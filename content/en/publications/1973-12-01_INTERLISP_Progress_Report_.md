---
title: "_INTERLISP Progress Report_"
date: '1973-12-01'
authors: 
    - Warren Teitelman
abstract: "INTERLISP (INTERactive LISP) is a LISP system currently implemented on the DEC PDP-10 under the BBN TENEX time sharing system{$<$}*R1{$>$}. INTERLISP is designed to provide the user access to the large virtual memory allowed by TENEX, with a relatively small penalty in speed (using special paging techniques described in {$<$}*R2{$>$}). Additional data types have been added, including strings, arrays, and hash association tables (hash links). The system includes a compatible compiler and interpreter. Machine code can be intermixed with INTERLISP expressions via the assemble directive of the compiler. The compiler also contains a facility for 'block compilation' which allows a group of functions to be compiled as a unit, suppressing internal names. Each successive level of computation, from interpreted through compiled, to block-compiled provides greater speed at a cost of debugging ease."
---

