---
title: "_LP_LISP_: Literate Programming for _Lisp_"
date: '2010-10-19'
authors: 
    - Roy M. Turner
abstract: "Writing a program and writing its documentation are often considered two separate tasks, leading to several problems: the documentation may never be written; when it is, it may be an afterthought; and when the program is modified, the needed changes to the documentation may be overlooked. Literate programming (LP), introduced by Donald Knuth, views a program and its documentation as an integrated whole: they are written together to inform both the computer and human readers. LP tools then extract the code for the computer and the documentation for further document processing. Unfortunately, existing LP tools are much more suited for compiled languages, where there is already a step between coding and executing and debugging the code. Lisp programming typically involved incremental development and testing, often highly interleaving coding with running portions of the code. Thus LP tools inject an artificial impediment into this process. LP/Lisp is a new LP tool designed specifically for Lisp and the usual style of programming using Lisp. The literate programming file is the Lisp file; LP markup and text resides in Lisp comments, where it does not interfere with running the code. LP/Lisp provided the usual literate programming services, such as code typesetting, syntactic sugaring, and the ability to split the code for expository purposes (a 'chunk' mechanism). LP/Lisp, itself written in Lisp, is run on the code to produce the documentation."
---

