---
title: "Fast _Generic Dispatch_ for _Common Lisp_"
date: '2014-08-14'
authors: 
    - Robert Strandh
abstract: "We describe a technique for generic dispatch that is adapted to modern computers where accessing memory is potentially quite expensive. Instead of the traditional hashing scheme used by PCL [6], we assign a unique number to each class, and the dispatch consists of comparisons of the number assigned to an instance with a certain number of (usually small) constant integers. While our implementation (SICL) is not yet in a state where we are able to get exact performance figures, a conservative simulation suggests that our technique is significantly faster than the one used in SBCL, which uses PCL, and indeed faster than the technique used by most high-performance Common Lisp implementations. Furthermore, existing work [7] using a similar technique in the context of static languages suggests that perfomance can improve significantly compared to table-based techniques."
---

