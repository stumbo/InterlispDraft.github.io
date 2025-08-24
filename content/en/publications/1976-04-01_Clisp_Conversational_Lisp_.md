---
title: "Clisp: _Conversational Lisp_"
date: '1976-04-01'
authors: 
    - Warren Teitelman
abstract: "Clisp is an attempt to make Lisp programs easier to read and write by extending the syntax of Lisp to include infix operators, IF-THEN statements, FOR-DO-WHILE statements, and similar Algol-like constructs, without changing the structure or representation of the language. Clisp is implemented through Lisp's error handling machinery, rather than by modifying the interpreter. When an expression is encountered whose evaluation causes an error, the expression is scanned for possible Clisp constructs, which are then converted to the equivalent Lisp expressions. Thus, users can freely intermix Lisp and Clisp without ut having to distinguish which is which. Emphasis in the design and development of Clisp has been on the system aspects of such a facility, with the goal of producing a useful tool, not just another language. To this end, Clisp includes interactive error correction and many 'do-what-I-mean' features."
---

