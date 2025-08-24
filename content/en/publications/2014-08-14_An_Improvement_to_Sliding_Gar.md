---
title: "An _Improvement_ to _Sliding Garbage Collection_"
date: '2014-08-14'
authors: 
    - Robert Strandh
abstract: "Garbage collection algorithms are divided into three main categories, namely mark-and-sweep, mark-and-compact, and copying collectors. The collectors in the mark-and-compact category are frequently overlooked, perhaps because they have traditionally been associated with greater cost than collectors in the other categories. Among the compacting collectors, the sliding collector has some advantages in that it preserves the relative age of objects. The main problem with the traditional sliding collector by Haddon and Waite [4] is that building address-forwarding tables is costly. We suggest an improvement to the existing algorithm that reverses the order between building the forwarding table and moving the objects. Our method improves performance of building the table, making the sliding collector a better contestant for young generations of objects (nurseries)."
---

