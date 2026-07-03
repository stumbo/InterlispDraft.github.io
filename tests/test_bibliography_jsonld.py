"""
tests/test_bibliography_jsonld.py
==================================
Validates the JSON-LD structured data emitted by
``layouts/_partials/bibliography-json-ld.html`` for every Schema.org type
used in the Interlisp bibliography.

How it works
------------
Each ``ZTEST-*.md`` fixture in ``tests/fixtures/bibliography/`` is the
**mock input**: it provides fully-controlled front-matter values that Hugo
feeds into the template.  A test-environment Hugo build mounts those fixtures
into the content tree without touching production content.  The tests then
read the rendered ``tests/public_test/history/bibliography/<slug>/index.html``,
extract the ``<script type="application/ld+json">`` block, and assert that the
resulting JSON-LD object has the correct Schema.org ``@type`` and every
type-specific field.

Fixture files (mock inputs)
---------------------------
    tests/fixtures/bibliography/ZTEST-JOURNAL.md     -> article-journal
    tests/fixtures/bibliography/ZTEST-MAGAZINE.md    -> article-magazine
    tests/fixtures/bibliography/ZTEST-CONFERENCE.md  -> paper-conference
    tests/fixtures/bibliography/ZTEST-BOOK.md        -> book
    tests/fixtures/bibliography/ZTEST-CHAPTER.md     -> chapter
    tests/fixtures/bibliography/ZTEST-REPORT.md      -> report
    tests/fixtures/bibliography/ZTEST-THESIS.md      -> thesis
    tests/fixtures/bibliography/ZTEST-PATENT.md      -> patent
    tests/fixtures/bibliography/ZTEST-WEBPAGE.md     -> webpage
    tests/fixtures/bibliography/ZTEST-BLOG.md        -> post-weblog
    tests/fixtures/bibliography/ZTEST-VIDEO.md       -> motion_picture
    tests/fixtures/bibliography/ZTEST-SOFTWARE.md    -> software
    tests/fixtures/bibliography/ZTEST-ENCYCLOPEDIA.md -> entry-encyclopedia
    tests/fixtures/bibliography/ZTEST-MESSAGE.md     -> personal_communication
    tests/fixtures/bibliography/ZTEST-NO-URLS.md     -> (sameAs absent edge case)

Hugo build
----------
The session-scoped ``_hugo_build`` fixture runs:

    hugo --environment testing --destination tests/public_test

The ``config/testing/hugo.yaml`` environment mounts ``tests/fixtures/bibliography/``
into the content tree via Hugo module mounts.  Test output lands in
``tests/public_test/``, which is gitignored and never deployed.

A rebuild is triggered automatically when any template or fixture file is
newer than the most recent test output file.  Set the environment variable
``PYTEST_FORCE_HUGO_BUILD=1`` to force a rebuild regardless.

Prerequisites
-------------
    pip install pytest    # only stdlib + pytest are required

Usage
-----
    # From the repository root:
    pytest tests/test_bibliography_jsonld.py -v

    # Force a fresh Hugo test build before running:
    PYTEST_FORCE_HUGO_BUILD=1 pytest tests/test_bibliography_jsonld.py -v
"""

import functools
import json
import os
import subprocess
from html.parser import HTMLParser
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
TEST_PUBLIC = REPO_ROOT / "tests" / "public_test"
BIB_PUBLIC = TEST_PUBLIC / "history" / "bibliography"
FIXTURES_DIR = REPO_ROOT / "tests" / "fixtures" / "bibliography"

# Hugo lowercases the filename slug when generating URLs.
FIXTURE_SLUGS = [
    "ztest-journal",
    "ztest-magazine",
    "ztest-conference",
    "ztest-book",
    "ztest-chapter",
    "ztest-report",
    "ztest-thesis",
    "ztest-patent",
    "ztest-webpage",
    "ztest-blog",
    "ztest-video",
    "ztest-software",
    "ztest-encyclopedia",
    "ztest-message",
    "ztest-no-urls",
]


# ---------------------------------------------------------------------------
# Staleness check
# ---------------------------------------------------------------------------

def _needs_rebuild() -> bool:
    """Return True when the test output is absent or older than any source file.

    Source files watched: all Hugo templates, the test fixtures, and the
    testing environment config.  Controlled by the ``PYTEST_FORCE_HUGO_BUILD``
    environment variable (any non-empty value forces a rebuild).
    """
    if os.environ.get("PYTEST_FORCE_HUGO_BUILD"):
        return True

    html_files = list(BIB_PUBLIC.rglob("index.html"))
    if not html_files:
        return True

    oldest_output = min(f.stat().st_mtime for f in html_files)

    watched = [
        REPO_ROOT / "layouts",
        REPO_ROOT / "config" / "testing",
        FIXTURES_DIR,
    ]
    for source in watched:
        for path in source.rglob("*"):
            if path.is_file() and path.stat().st_mtime > oldest_output:
                return True

    return False


# ---------------------------------------------------------------------------
# HTML helper – extract <script type="application/ld+json"> blocks
# ---------------------------------------------------------------------------


class _JSONLDExtractor(HTMLParser):
    """Pull raw text out of every ``application/ld+json`` script element."""

    def __init__(self) -> None:
        super().__init__()
        self._in_jsonld: bool = False
        self.blocks: list[str] = []
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == "script" and dict(attrs).get("type") == "application/ld+json":
            self._in_jsonld = True
            self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.blocks.append("".join(self._buf))

    def handle_data(self, data: str) -> None:
        if self._in_jsonld:
            self._buf.append(data)


@functools.lru_cache(maxsize=None)
def _load_jsonld(slug: str) -> dict:
    """Return the Schema.org JSON-LD dict from the built bibliography page *slug*.

    Results are cached so each fixture HTML file is read and parsed exactly
    once per test session regardless of how many test methods reference it.

    Skips (not fails) when the built page is absent; the session fixture
    ``_hugo_build`` normally ensures the build runs before any test.
    """
    path = BIB_PUBLIC / slug / "index.html"
    if not path.exists():
        pytest.skip(
            f"Built page not found: {path}\n"
            "Run 'hugo --environment testing --destination tests/public_test' "
            "from the repo root, then re-run the tests."
        )

    parser = _JSONLDExtractor()
    parser.feed(path.read_text(encoding="utf-8"))

    for raw in parser.blocks:
        try:
            data = json.loads(raw.strip())
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@context") == "https://schema.org":
            return data

    pytest.fail(f"No schema.org JSON-LD block found in {path}")


# ---------------------------------------------------------------------------
# Session-scoped Hugo build
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def _hugo_build() -> None:
    """Build the Hugo test site once per pytest session when sources have changed.

    Uses ``--environment testing`` which reads ``config/testing/hugo.yaml``,
    mounting ``tests/fixtures/bibliography/`` into the content tree and
    writing output to ``tests/public_test/``.

    Set ``PYTEST_FORCE_HUGO_BUILD=1`` to bypass the staleness check.
    """
    if not _needs_rebuild():
        return

    result = subprocess.run(
        [
            "hugo",
            "--environment", "testing",
            "--destination", "tests/public_test",
        ],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.fail(
            f"Hugo test build failed (exit {result.returncode}):\n"
            f"--- stdout ---\n{result.stdout}\n"
            f"--- stderr ---\n{result.stderr}"
        )
    if result.stderr:
        # Surface warnings without failing so they're visible in CI logs.
        print(f"\n[hugo warnings]\n{result.stderr}", flush=True)


# ---------------------------------------------------------------------------
# Shared assertion helpers
# ---------------------------------------------------------------------------


def _assert_base(ld: dict, expected_type: str, expected_name: str) -> None:
    """Assert the fields present on every single-page bibliography entry."""
    assert ld.get("@context") == "https://schema.org", (
        f"@context must be 'https://schema.org', got {ld.get('@context')!r}"
    )
    assert ld.get("@type") == expected_type, (
        f"@type must be {expected_type!r}, got {ld.get('@type')!r}"
    )
    assert ld.get("name") == expected_name, (
        f"name must be {expected_name!r}, got {ld.get('name')!r}"
    )
    assert ld.get("inLanguage") == "en-US", (
        f"inLanguage must be 'en-US', got {ld.get('inLanguage')!r}"
    )
    assert ld.get("url", "").endswith("/"), (
        f"url must end with '/', got {ld.get('url')!r}"
    )


def _assert_person(
    person: dict,
    expected_name: str,
    family: str | None = None,
    given: str | None = None,
) -> None:
    """Assert a Schema.org Person object."""
    assert person.get("@type") == "Person", (
        f"Person @type must be 'Person', got {person.get('@type')!r}"
    )
    assert person.get("name") == expected_name, (
        f"Person name must be {expected_name!r}, got {person.get('name')!r}"
    )
    if family is not None:
        assert person.get("familyName") == family, (
            f"familyName must be {family!r}, got {person.get('familyName')!r}"
        )
    if given is not None:
        assert person.get("givenName") == given, (
            f"givenName must be {given!r}, got {person.get('givenName')!r}"
        )


def _assert_org(obj: dict, expected_name: str) -> None:
    """Assert a Schema.org Organization object."""
    assert obj.get("@type") == "Organization", (
        f"Expected Organization, got @type={obj.get('@type')!r}"
    )
    assert obj.get("name") == expected_name, (
        f"Organization name must be {expected_name!r}, got {obj.get('name')!r}"
    )


# ===========================================================================
# Per-type test classes
# ===========================================================================


class TestScholarlyArticle:
    """article-journal → ScholarlyArticle

    Mock fixture: ZTEST-JOURNAL.md
    Authors: Smith, Alice J. | Jones, Bob
    Journal: Journal of Test Science  vol 5, issue 2, pp 45-67
    Concepts: Interlisp, ProgrammingLanguages  (tests about[] + keywords)
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-journal")["@type"] == "ScholarlyArticle"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-journal"), "ScholarlyArticle", "Test Scholarly Article")

    def test_date_published(self):
        assert _load_jsonld("ztest-journal")["datePublished"] == "2020-03-15"

    def test_date_modified(self):
        assert _load_jsonld("ztest-journal")["dateModified"] == "2023-01-10T00:00:00Z"

    def test_description_from_abstract(self):
        desc = _load_jsonld("ztest-journal").get("description", "")
        assert "journal article" in desc.lower()

    def test_authors_count_and_order(self):
        authors = _load_jsonld("ztest-journal")["author"]
        assert len(authors) == 2, f"Expected 2 authors, got {len(authors)}"
        # "Smith, Alice J." → givenName=Alice J., familyName=Smith
        _assert_person(authors[0], "Alice J. Smith", family="Smith", given="Alice J.")
        # "Jones, Bob" → givenName=Bob, familyName=Jones
        _assert_person(authors[1], "Bob Jones", family="Jones", given="Bob")

    def test_same_as_contains_both_urls(self):
        same_as = _load_jsonld("ztest-journal")["sameAs"]
        assert "https://example.com/journal-article" in same_as
        assert "https://www.zotero.org/groups/test/items/ZTESTJNL" in same_as

    def test_same_as_url_source_precedes_zotero(self):
        """url_source must appear before zotero_url in the sameAs array."""
        same_as = _load_jsonld("ztest-journal")["sameAs"]
        src_idx = same_as.index("https://example.com/journal-article")
        zoo_idx = same_as.index("https://www.zotero.org/groups/test/items/ZTESTJNL")
        assert src_idx < zoo_idx, "url_source should appear before zotero_url in sameAs"

    def test_periodical_is_part_of(self):
        is_part_of = _load_jsonld("ztest-journal")["isPartOf"]
        assert is_part_of["@type"] == "Periodical"
        assert is_part_of["name"] == "Journal of Test Science"

    def test_volume_number(self):
        assert _load_jsonld("ztest-journal")["volumeNumber"] == "5"

    def test_issue_number(self):
        assert _load_jsonld("ztest-journal")["issueNumber"] == "2"

    def test_pagination(self):
        assert _load_jsonld("ztest-journal")["pagination"] == "45-67"

    def test_about_defined_terms(self):
        about = _load_jsonld("ztest-journal")["about"]
        ids = [term["@id"] for term in about]
        assert "https://interlisp.org/concepts/#Interlisp" in ids
        assert "https://interlisp.org/concepts/#ProgrammingLanguages" in ids
        for term in about:
            assert term["@type"] == "DefinedTerm"
            assert term["inDefinedTermSet"] == "https://interlisp.org/data/cs-concepts.jsonld"
            assert "name" in term

    def test_keywords_from_concepts(self):
        keywords = _load_jsonld("ztest-journal")["keywords"]
        assert "Interlisp" in keywords
        assert "Programming Languages" in keywords


class TestMagazineArticle:
    """article-magazine → Article

    Mock fixture: ZTEST-MAGAZINE.md
    Maps to Schema.org Article (not ScholarlyArticle).
    Shares the same journal-style field block as article-journal.
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-magazine")["@type"] == "Article"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-magazine"), "Article", "Test Magazine Article")

    def test_author(self):
        authors = _load_jsonld("ztest-magazine")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Jane Doe", family="Doe", given="Jane")

    def test_periodical_is_part_of(self):
        is_part_of = _load_jsonld("ztest-magazine")["isPartOf"]
        assert is_part_of["@type"] == "Periodical"
        assert is_part_of["name"] == "Computing Monthly"

    def test_volume_issue_pagination(self):
        ld = _load_jsonld("ztest-magazine")
        assert ld["volumeNumber"] == "10"
        assert ld["issueNumber"] == "6"
        assert ld["pagination"] == "12-14"


class TestConferencePaper:
    """paper-conference → ScholarlyArticle

    Mock fixture: ZTEST-CONFERENCE.md
    Uses proceedings_title (isPartOf Book), publisher, and place
    (locationCreated Place).
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-conference")["@type"] == "ScholarlyArticle"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-conference"), "ScholarlyArticle", "Test Conference Paper")

    def test_proceedings_is_part_of(self):
        is_part_of = _load_jsonld("ztest-conference")["isPartOf"]
        assert is_part_of["@type"] == "Book"
        assert is_part_of["name"] == "Proceedings of the Test Conference 2019"

    def test_publisher(self):
        _assert_org(_load_jsonld("ztest-conference")["publisher"], "ACM")

    def test_location_created(self):
        """place front-matter field maps to locationCreated Place."""
        location = _load_jsonld("ztest-conference")["locationCreated"]
        assert location["@type"] == "Place"
        assert location["name"] == "San Francisco, CA"

    def test_authors_with_compound_given_name(self):
        """'Brown, Carol K.' splits to givenName='Carol K.', familyName='Brown'."""
        authors = _load_jsonld("ztest-conference")["author"]
        assert len(authors) == 2
        _assert_person(authors[0], "Carol K. Brown", family="Brown", given="Carol K.")
        _assert_person(authors[1], "David White", family="White", given="David")


class TestBook:
    """book → Book

    Mock fixture: ZTEST-BOOK.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-book")["@type"] == "Book"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-book"), "Book", "Test Book Title")

    def test_publisher(self):
        _assert_org(_load_jsonld("ztest-book")["publisher"], "Test Publisher")

    def test_author(self):
        authors = _load_jsonld("ztest-book")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Test Author", family="Author", given="Test")

    def test_same_as_order(self):
        """url_source must be the first element; zotero_url must be the second."""
        same_as = _load_jsonld("ztest-book")["sameAs"]
        assert same_as[0] == "https://example.com/book"
        assert same_as[1] == "https://www.zotero.org/groups/test/items/ZTESTBOOK"


class TestChapter:
    """chapter → Chapter

    Mock fixture: ZTEST-CHAPTER.md
    isPartOf is a Book that also carries a nested publisher Organization.
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-chapter")["@type"] == "Chapter"

    def test_is_part_of_book(self):
        parent = _load_jsonld("ztest-chapter")["isPartOf"]
        assert parent["@type"] == "Book"
        assert parent["name"] == "Test Book of Chapters"

    def test_parent_book_publisher(self):
        """Publisher is nested inside the isPartOf Book object."""
        parent = _load_jsonld("ztest-chapter")["isPartOf"]
        _assert_org(parent["publisher"], "Chapter Publisher")

    def test_pagination(self):
        assert _load_jsonld("ztest-chapter")["pagination"] == "100-120"

    def test_editor(self):
        editors = _load_jsonld("ztest-chapter")["editor"]
        assert len(editors) == 1
        _assert_person(editors[0], "Test Editor", family="Editor", given="Test")

    def test_author(self):
        authors = _load_jsonld("ztest-chapter")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Test Writer", family="Writer", given="Test")


class TestReport:
    """report → Report

    Mock fixture: ZTEST-REPORT.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-report")["@type"] == "Report"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-report"), "Report", "Test Technical Report")

    def test_publisher(self):
        _assert_org(_load_jsonld("ztest-report")["publisher"], "Test Research Lab")

    def test_author(self):
        authors = _load_jsonld("ztest-report")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Test Researcher", family="Researcher", given="Test")


class TestThesis:
    """thesis → Thesis

    Mock fixture: ZTEST-THESIS.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-thesis")["@type"] == "Thesis"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-thesis"), "Thesis", "Test Doctoral Thesis")

    def test_source_organization(self):
        org = _load_jsonld("ztest-thesis")["sourceOrganization"]
        assert org["@type"] == "CollegeOrUniversity"
        assert org["name"] == "Test University"

    def test_author(self):
        authors = _load_jsonld("ztest-thesis")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Test Student", family="Student", given="Test")

    def test_no_publisher_key(self):
        """Theses use sourceOrganization, not publisher."""
        assert "publisher" not in _load_jsonld("ztest-thesis"), (
            "Thesis should use sourceOrganization, not publisher"
        )


class TestPatent:
    """patent → CreativeWork + additionalType "Patent"

    Mock fixture: ZTEST-PATENT.md
    Verifies both PropertyValue identifier objects, copyrightHolder (assignee),
    and validIn DefinedRegion (issuing authority).
    """

    def test_schema_type_is_creative_work(self):
        assert _load_jsonld("ztest-patent")["@type"] == "CreativeWork"

    def test_additional_type_is_patent(self):
        assert _load_jsonld("ztest-patent")["additionalType"] == "Patent"

    def test_patent_number_identifier(self):
        identifiers = _load_jsonld("ztest-patent")["identifier"]
        match = next(
            (i for i in identifiers if i.get("propertyID") == "patent-number"), None
        )
        assert match is not None, "No 'patent-number' identifier found"
        assert match["@type"] == "PropertyValue"
        assert match["value"] == "US9876543B2"

    def test_application_number_identifier(self):
        identifiers = _load_jsonld("ztest-patent")["identifier"]
        match = next(
            (i for i in identifiers if i.get("propertyID") == "application-number"), None
        )
        assert match is not None, "No 'application-number' identifier found"
        assert match["@type"] == "PropertyValue"
        assert match["value"] == "US12345678"

    def test_assignee_maps_to_copyright_holder(self):
        """Patent assignee (rights owner) maps to copyrightHolder, not funder."""
        holder = _load_jsonld("ztest-patent")["copyrightHolder"]
        _assert_org(holder, "Test Corporation")

    def test_issuing_authority_maps_to_valid_in(self):
        """Issuing authority (jurisdiction) maps to validIn DefinedRegion."""
        region = _load_jsonld("ztest-patent")["validIn"]
        assert region["@type"] == "DefinedRegion"
        assert region["name"] == "United States"

    def test_author(self):
        authors = _load_jsonld("ztest-patent")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Test Inventor", family="Inventor", given="Test")


class TestWebPage:
    """webpage → WebPage

    Mock fixture: ZTEST-WEBPAGE.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-webpage")["@type"] == "WebPage"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-webpage"), "WebPage", "Test Web Page")

    def test_is_part_of_website(self):
        parent = _load_jsonld("ztest-webpage")["isPartOf"]
        assert parent["@type"] == "WebSite"
        assert parent["name"] == "Test Website"


class TestBlogPosting:
    """post-weblog → BlogPosting

    Mock fixture: ZTEST-BLOG.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-blog")["@type"] == "BlogPosting"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-blog"), "BlogPosting", "Test Blog Post")

    def test_is_part_of_blog(self):
        parent = _load_jsonld("ztest-blog")["isPartOf"]
        assert parent["@type"] == "Blog"
        assert parent["name"] == "Test Tech Blog"


class TestVideoObject:
    """motion_picture → VideoObject

    Mock fixture: ZTEST-VIDEO.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-video")["@type"] == "VideoObject"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-video"), "VideoObject", "Test Motion Picture")

    def test_production_company(self):
        _assert_org(_load_jsonld("ztest-video")["productionCompany"], "Test Film Studio")

    def test_encoding_format(self):
        assert _load_jsonld("ztest-video")["encodingFormat"] == "MP4"

    def test_part_of_series(self):
        series = _load_jsonld("ztest-video")["partOfSeries"]
        assert series["@type"] == "CreativeWorkSeries"
        assert series["name"] == "Test Film Series"


class TestSoftwareSourceCode:
    """software → SoftwareSourceCode

    Mock fixture: ZTEST-SOFTWARE.md
    Also validates the single-name (no comma) author edge case via the
    "Singularity" author entry, which has no family/given split.
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-software")["@type"] == "SoftwareSourceCode"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-software"), "SoftwareSourceCode", "Test Software")

    def test_two_author_objects_present(self):
        assert len(_load_jsonld("ztest-software")["author"]) == 2

    def test_author_with_comma_split(self):
        """'Developer, Test' → givenName='Test', familyName='Developer'."""
        authors = _load_jsonld("ztest-software")["author"]
        _assert_person(authors[0], "Test Developer", family="Developer", given="Test")

    def test_author_without_comma_has_only_name(self):
        """'Singularity' (no comma) → only 'name' key, no familyName/givenName."""
        authors = _load_jsonld("ztest-software")["author"]
        single = next(
            (a for a in authors if a["name"] == "Singularity"),
            None,
        )
        assert single is not None, "'Singularity' author not found in author array"
        assert single["@type"] == "Person"
        assert "familyName" not in single, (
            "A name without a comma must not produce a familyName key"
        )
        assert "givenName" not in single, (
            "A name without a comma must not produce a givenName key"
        )


class TestEncyclopediaEntry:
    """entry-encyclopedia → Article with isPartOf Book

    Mock fixture: ZTEST-ENCYCLOPEDIA.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-encyclopedia")["@type"] == "Article"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-encyclopedia"), "Article", "Test Encyclopedia Entry")

    def test_is_part_of_book(self):
        """encyclopedia_title maps to isPartOf Book."""
        parent = _load_jsonld("ztest-encyclopedia")["isPartOf"]
        assert parent["@type"] == "Book"
        assert parent["name"] == "Encyclopedia of Test Computing"


class TestPersonalCommunication:
    """personal_communication → Message

    Mock fixture: ZTEST-MESSAGE.md
    """

    def test_schema_type(self):
        assert _load_jsonld("ztest-message")["@type"] == "Message"

    def test_base_fields(self):
        _assert_base(_load_jsonld("ztest-message"), "Message", "Test Personal Communication")

    def test_author(self):
        authors = _load_jsonld("ztest-message")["author"]
        assert len(authors) == 1
        _assert_person(authors[0], "Test Sender", family="Sender", given="Test")


# ===========================================================================
# Cross-cutting / edge-case tests
# ===========================================================================


class TestCommonFields:
    """Shared field correctness and edge cases that span multiple types."""

    def test_date_published_iso_format(self):
        """datePublished is always YYYY-MM-DD regardless of input format."""
        cases = [
            ("ztest-journal", "2020-03-15"),
            ("ztest-book", "1995-01-01"),
            ("ztest-thesis", "2010-05-01"),
        ]
        for slug, expected in cases:
            ld = _load_jsonld(slug)
            assert ld.get("datePublished") == expected, (
                f"{slug}: expected datePublished={expected!r}, "
                f"got {ld.get('datePublished')!r}"
            )

    def test_date_modified_preserved_verbatim(self):
        """dateModified is the raw lastmod string from front matter."""
        assert _load_jsonld("ztest-report")["dateModified"] == "2023-04-01T00:00:00Z"

    def test_description_from_abstract(self):
        """The abstract front-matter field becomes the JSON-LD description."""
        assert "test abstract for a book" in (
            _load_jsonld("ztest-book").get("description", "").lower()
        )

    def test_in_language_always_en_us(self):
        """Every bibliography page must carry inLanguage='en-US'."""
        for slug in FIXTURE_SLUGS:
            assert _load_jsonld(slug).get("inLanguage") == "en-US", (
                f"{slug}: inLanguage must be 'en-US'"
            )

    def test_context_always_schema_org(self):
        """Every bibliography page must declare @context='https://schema.org'."""
        for slug in FIXTURE_SLUGS:
            assert _load_jsonld(slug).get("@context") == "https://schema.org", (
                f"{slug}: @context must be 'https://schema.org'"
            )

    def test_same_as_absent_when_no_urls(self):
        """When neither url_source nor zotero_url is set, sameAs must be omitted."""
        ld = _load_jsonld("ztest-no-urls")
        assert "sameAs" not in ld, (
            f"sameAs must not be present when no URLs are set, got {ld.get('sameAs')!r}"
        )

    def test_journal_keys_absent_from_non_journal_types(self):
        """Journal-specific keys must not bleed into Book, Thesis, or Report pages."""
        journal_keys = ("volumeNumber", "issueNumber", "pagination")
        for slug in ("ztest-book", "ztest-thesis", "ztest-report"):
            ld = _load_jsonld(slug)
            for key in journal_keys:
                assert key not in ld, (
                    f"{slug} must not have journal key '{key}'"
                )

    def test_conference_keys_absent_from_journal(self):
        """Conference-specific keys must not appear on journal article pages."""
        ld = _load_jsonld("ztest-journal")
        assert "locationCreated" not in ld, (
            "locationCreated must not appear on journal article pages"
        )


class TestCollectionPage:
    """The bibliography section page emits CollectionPage + ItemList JSON-LD."""

    def test_schema_type(self):
        ld = _load_jsonld_section()
        assert ld["@type"] == "CollectionPage"

    def test_context(self):
        assert _load_jsonld_section()["@context"] == "https://schema.org"

    def test_in_language(self):
        assert _load_jsonld_section()["inLanguage"] == "en-US"

    def test_main_entity_is_item_list(self):
        main = _load_jsonld_section()["mainEntity"]
        assert main["@type"] == "ItemList"

    def test_item_list_contains_fixture_entries(self):
        """The ItemList must include at least the fixture pages."""
        items = _load_jsonld_section()["mainEntity"]["itemListElement"]
        urls = {item["url"] for item in items}
        # Every fixture page should appear as a list item.
        for slug in FIXTURE_SLUGS:
            assert any(slug in u for u in urls), (
                f"ItemList missing entry for fixture slug '{slug}'"
            )

    def test_item_list_positions_are_sequential(self):
        items = _load_jsonld_section()["mainEntity"]["itemListElement"]
        positions = [item["position"] for item in items]
        assert positions == list(range(1, len(items) + 1)), (
            "ItemList positions must be consecutive integers starting at 1"
        )

    def test_number_of_items_matches_list_length(self):
        main = _load_jsonld_section()["mainEntity"]
        assert main["numberOfItems"] == len(main["itemListElement"])


@functools.lru_cache(maxsize=1)
def _load_jsonld_section() -> dict:
    """Return the Schema.org JSON-LD dict from the bibliography section index page."""
    path = TEST_PUBLIC / "history" / "bibliography" / "index.html"
    if not path.exists():
        pytest.skip(f"Section index not found: {path}")

    parser = _JSONLDExtractor()
    parser.feed(path.read_text(encoding="utf-8"))

    for raw in parser.blocks:
        try:
            data = json.loads(raw.strip())
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@type") == "CollectionPage":
            return data

    pytest.fail(f"No CollectionPage JSON-LD block found in {path}")
