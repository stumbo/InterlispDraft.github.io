---
title: "Linkers and Loaders"
date: '2003-01-01'
authors: 
    - David W. Barron
abstract: "Terminology concerning linkers and loaders is confusing, having changed over the years as technology has changed. In older mainframe operating systems, processing of a program between compiling and execution took place in two distinct stages. The function of the linker (or linkage editor) was to combine a number of independently compiled or assembled object files into a single load module, resolving cross-references and incorporating routines from libraries as required. The loader then prepared this module for execution, physically loaded it into memeory, and started execution. Early versions of Unix (q.v.) blurred this distinction: the functions of the linker were incorporated into the C (q.v.) compiler in what was confusingly called the 'load phase,' and the actual loading was done as part of the 'exec,' operation that installed a new process image for execution."
---

