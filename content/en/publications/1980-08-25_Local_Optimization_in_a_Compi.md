---
title: "Local Optimization in a Compiler for Stack-Based _Lisp_ Machines"
date: '1980-08-25'
authors: 
    - Larry M. Masinter
    - L. Peter Deutsch
abstract: "We describe the local optimization phase of a compiler for translating the INTERLISP dialect of LISP into stack-architecture (0-address) instruction sets. We discuss the general organization of the compiler, and then describe the set of optimization techniques found most useful, based on empirical results gathered by compiling a large set of programs. The compiler and optimization phase are machine independent, in that they generate a stream of instructions for an abstract stack machine, which an assembler subsequently turns into the actual machine instructions. The compiler has been in successful use for several years, producing code for two different instruction sets."
---

