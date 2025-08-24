---
title: "Format-Directed List Processing in _LISP_"
date: '1966-01-01'
authors: 
    - Daniel G. Bobrow
    - Warren Teitelman
abstract: "This article describes a notation and a programming language for expressing, from within a LISP system, string transformations such as those performed in COMIT or SNOBOL. A simple transformation (or transformation rule) is specified by providing a pattern which must match the structure to be transformed and a format which specifies how to construct a new structure according to the segmentation specified by the pattern. The patterns and formats are greatly generalized versions of the left-half and right-half rules of COMIT and SNOBOL. For example, elementary patterns and formats can be variable names, results of computations, disjunctive sets, or repeating subpatterns; predicates can be associated with elementary patterns which check relationships among separated elements of the match; it is no longer necessary to restrict the operations to linear strings since elementary patterns can themselves match structures. The FLIP language has been implemented in LISP 1.5, and has been successfully used in such disparate tasks as editing LISP functions and parsing Kleene regular expressions."
---

