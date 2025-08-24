---
title: "On Compiling Embedded Languages in _LISP_"
date: '1980-08-25'
authors: 
    - Par Emanuelson
    - Anders Haraldsson
abstract: "In INTERLISP we find a number of embedded languages such as the iterative statement and the pattern match facility in the CLISP package, the editor and makefile languages and so forth. We will in this paper concentrate on the problem of extending the LISP language and discuss a method to compile such extensions. We propose the language to be implemented through an interpreter (written in LISP) and that compilation of statements in such an embedded language is done through partial evaluation. The interpreter is partially evaluated with respect to the actual statements, and an object program in LISP is obtained. This LISP code can further be compiled to machine code by the standard LISP compiler. We have implemented the iterative statement and a CLISP-like pattern matcher and used a program manipulation system to generate object programs in LISP. Comparisons will be made with the corresponding INTERLISP implementations, which use special purpose compilers in order to generate the LISP code."
---

