---
title: "An Implementation of Portable Standard _LISP_ on the _BBN_ Butterfly"
date: '1988-01-01'
authors: 
    - Mark Swanson
    - Robert Kessler
    - Gary Lindstrom
abstract: "An implementation of the Portable Standard Lisp (PSL) on the BBN Butterfly is described. Butterfly PSL is identical, syntactically and semantically, to implementations of PSL currently available on the VAX, Gould, and many 68000-based machines, except for the differences discussed in this paper. The differences include the addition of the future and touch constructs for explicit parallelism and an extension of the fluid binding mechanism to support the multiple environments required by concurrent tasks. As with all other PSL implementations, full compilation to machine code of the basic system and application source code is the normal mode, in contrast to the previous byte-code interpreter efforts. Also discussed are other required changes to the PSL system not visible in the syntax or semantics, e.g., compiler support for the future construct. Finally, the underlying hardware is described, and timings for basic operations and speedup results for two examples are given."
---

