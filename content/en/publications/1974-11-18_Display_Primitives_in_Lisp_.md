---
title: "Display Primitives in _Lisp_"
date: '1974-11-18'
authors: 
    - P. Deutsch
abstract: "Several conflicting goal must be resolved in deciding on a set of display facilities for Lisp: ease of lisp, efficient access to hardware facilities, and device- and system-independence. This memo suggests a set of facilities constructed in two layers: a lower layer that gives direct access to the Alto bitmap capability, while retaining Lisp's tradition of freeing the programmer from storage allocation worries, and an upper Iayer that uses the lower (on the Alto) or a character-stream protocol (for VTS, on MAXC) to provide for writing strings, scrolling, edting, etc. on the screen,"
---

