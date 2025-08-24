---
title: "Garbage Collection in a Large _LISP_ System"
date: '1984-08-06'
authors: 
    - David A. Moon
abstract: "This paper discusses garbage collection techniques used in a high-performance Lisp implementation with a large virtual memory, the Symbolics 3600. Particular attention is paid to practical issues and experience. In a large system problems of scale appear and the most straightforward garbage-collection techniques do not work well. Many of these problems involve the interaction of the garbage collector with demand-paged virtual memory. Some of the solutions adopted in the 3600 are presented, including incremental copying garbage collection, approximately depth-first copying, ephemeral objects, tagged architecture, and hardware assists. We discuss techniques for improving the efficiency of garbage collection by recognizing that objects in the Lisp world have a variety of lifetimes. The importance of designing the architecture and the hardware to facilitate garbage collection is stressed."
---

