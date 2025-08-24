---
title: "Storage _Management_ in _LISP_"
date: '1966-06-01'
authors: 
    - Daniel G. Bobrow
abstract: "Storage allocation, maintenance, and reclamation are handled automatically in LISP systems.  Storage is allocated as needed, and a garbage collection process periodically reclaims storage no longer in use.  A number of different garbage collection algorithms are described.  A common property of most of these algorithms is that during garbage collection all other computation ceases.  This is an untenable situation for programs which must respond to real time interrupts.  The paper concludes with a proposal for an incremental garbage collection scheme which allows simultaneous computation and storage reclamation."
---

