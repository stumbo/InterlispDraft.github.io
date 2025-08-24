---
title: "Futures and Multiple Values in Parallel _Lisp_"
date: '1995-05-05'
authors: 
    - Tanaka Tomoyuki
    - Uzuhara Shigeru
abstract: "We consider the impact of introducing the future construct to the multiple value facility in Lisp (Common Lisp and Scheme). A natural way to accommodate this problem is by modifying the implementation of futures so that one future object returns (or resolves to) multiple values instead of one. We first show how a such straightforward modification fails to maintain the crucial characteristic of futures, namely that inserting futures in a functional program does not alter the the result of the computation. A straightforward modification may result in wrong number of values. We then present two methods which we call the mv-context method and the mv-p flag method to overcome this problem. Both of these methods have been tested in TOP-1 Common Lisp, an implementation of a parallel Common Lisp on the TOP-1 multiprocessor workstation. To our knowledge, this problem has never been analyzed nor solved in an implementation of parallel Lisp. We also present the technique of future chain elimination which avoids creation of unnecessary futures and processes at run-time, which was inspired by this solution."
---

