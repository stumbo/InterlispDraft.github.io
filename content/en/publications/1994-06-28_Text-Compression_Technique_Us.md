---
title: "Text-Compression Technique Using Frequency-Ordered Array of Word-Number Mappers"
date: '1994-06-28'
authors: 
    - Ronald M. Kaplan
    - John T. III Maxwell
abstract: "A text-compression technique utilizes a plurality of word-number mappers ('WNMs') in a frequency-ordered hierarchical structure. The particular structure of the set of WNMs depends on the specific encoding regime, but can be summarized as follows. Each WNM in the set is characterized by an ordinal WNM number and a WNM size (maximum number of tokens) that is in general a non-decreasing function of the WNM number. A given token is assigned a number pair, the first being one of the WNM numbers, and the second being the token's position or number in that WNM. Typically, the most frequently occurring tokens are mapped with a smaller-numbered WNM. The set of WNMs is generated on a first pass through the database to be compressed. The database is parsed into tokens, and a rank-order list based on the frequency of occurrence is generated. This list is partitioned in a manner to define the set of WNMs. Actual compression of the data base occurs on a second pass, using the set of WNMs generated on the first pass. The database is parsed into tokens, and for each token, the set of WNMs is searched to find the token. Once the token is found, it is assigned the appropriate number pair and is encoded. This proceeds until the entire database has been compressed."
---

