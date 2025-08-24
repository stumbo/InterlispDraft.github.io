---
title: "_COMPARESOURCES_"
date: '2021-12-01'
authors: 
    - van Melle
    - Bill
    - Kaplan
    - Ronald M.
abstract: "COMPARESOURCES is a program for comparing two versions of a Lisp source file for differences. The comparison is completely brute-force: COMPARESOURCES reads the complete contents of both files, and compares all the expressions for differences. The files need not be ones produced by MAKEFILE, as COMPARESOURCES reads the contents with READFILE; however, the program is tuned for files of the type produced by MAKEFILE."
---

