---
title: "Isolation and Analysis of Optimization Errors"
date: '1993-06-01'
authors: 
    - Mickey R. Boyd
    - David B. Whalley
abstract: "This paper describes two related tools developed to support the isolation and analysts of optimization errors in the vpo optimizer. Both tools rely on vpo identifying sequences of changes, referred to as transformations. that result in semantically equivalent (and usually improved) code. One tool determines the first transfer. motion that causes incorrect output of the execution of the compiled program. This tool not only automatically isolates the illegal transformation, but also identifies the location and instant the transformation is performed in vpo. To assist in the analysis of an optimization error, a graphical optimization viewer was also implemented that can display the state of the generated instructions before and after each transformation performed by vpo. Unique features of the optimization viewer include reverse viewing (or undoing) of transformations and the ability to stop at breakpoints associated with the generated instructions. Both tools are useful independently. Together these tools form a powerful environment for facilitating the retargeting of vpo to a new machine and supporting experimentation with new optimizations. In addition, the optimization viewercan be used as a teaching aid in compiler classes."
---

