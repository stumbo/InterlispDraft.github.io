---
title: "A Note on Hash Linking"
date: '1975-07-01'
authors: 
    - Daniel G. Bobrow
abstract: "In current machine designs, a machine address gives the user direct access to a single piece of information, namely the contents of that machine word. This note is based on the observation that it is often useful to associate additional information, with some (relatively few) address locations determined at run time, without the necessity of preallocating the storage at all possible such addresses. That is, it can be useful to have an effective extra bit, field, or address in some words without every word having to contain a bit (or bits) to mark this as a special case. The key idea is that this extra associated information can be found by a table search. Although it could be found by any search technique (e.g. linear, binary sorted, etc.), we suggest that an appropriate low overhead mechanism is to use hash search on a table in which the key is the address of the cell to be augmented."
---

