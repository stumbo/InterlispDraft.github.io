---
title: "A _LISP_ Compiler Producing Compact Code"
date: '1980-08-25'
authors: 
    - William Rowan
abstract: "A compiler has been written which compiles MACLISP into a compact intermediate language called 1-code, and an 1-code interpreter has been incorporated into an existing LISP system. The 1-code “machine” has a simple stack architecture and an instruction set specifically designed for LISP. Compiled programs consist of a string of eight-bit bytes of 1-code, and a local table of quantities used by the compiled code. The system has been used to compile most of the MACSYMA system, and algebraic expressions have been successfully evaluated. The system is about three times faster than interpreted LISP, and about 8 times more compact, if the 1-code and local table are compared in size to the dotted pairs needed for the uncompiled version. The possibility of enhancing the system to a true machine-independent LISP compiler is considered. In particular, the problem of varying instruction quantization size is examined, and a method is given for running 1-code programs on machines with different byte sizes."
---

