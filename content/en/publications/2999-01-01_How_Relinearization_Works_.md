---
title: "How _Relinearization Works_"
date: '2999-01-01'
authors: 
    - NA
abstract: "The process by which SEdit optimizes formatting recomputation is strange and wonderful, so this is a long overdue attempt at explaining it. We will start with a quick recap of SEdit’s formatting model and the responsibilities of three node type methods: assign-format, compute-format-values, and linearize. We then describe the assumptions SEdit makes about when these have to be redone, and then describe the algorithm it uses to achieve this. We’ll only go as far as getting the linear form fixed up; the step from there to updating the bits in the window is a whole ’nother story..."
---

