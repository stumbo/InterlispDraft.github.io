---
title: "Implementation of _Interlisp_ on the _VAX_"
date: '1982-08-01'
authors: 
    - Raymond L. Bates
    - David Dyer
    - Johannes A. G. M. Koomen
abstract: "This paper presents some of the issues involved in implementing Interlisp [19] on a VAX computer [24] with the goal of producing a version that runs under UNIX[17], specifically Berkeley VM/UNIX. This implementation has the following goals: • To be compatible with and functionally equivalent to Interlisp-10. • To serve as a basis for future Interlisp implementations on other mainframe computers. This goal requires that the implementation to be portable. • To support a large virtual address space. • To achieve a reasonable speed. The implementation draws directly from three sources, Interlisp-10 [19], Interlisp-D [5], and Multilisp [12]. Interlisp-10, the progenitor of all Interlisps, runs on the PDP-10 under the TENEX [2] and TOPS-20 operating systems. Interlisp-D, developed at Xerox Palo Alto Research Center, runs on personal computers also developed at PARC. Multilisp, developed at the University of British Columbia, is a portable interpreter containing a kernel of Interlisp, written in Pascal [9] and running on the IBM Series/370 and the VAX. The Interlisp-VAX implementation relies heavily on these implementations. In turn, Interlisp-D and Multilisp were developed from The Interlisp Virtual Machine Specification [15] by J Moore (subsequently referred to as the VM specification), which discusses what is needed to implement an Interlisp by describing an Interlisp Virtual Machine from the implementors' point of view. Approximately six man-years of effort have been spent exclusively in developing Interlisp-VAX, plus the benefit of many years of development for the previous Interlisp implementations."
---

