---
title: "Compact _Encodings_ of _List Structure_"
date: '1979-10-01'
authors: 
    - Daniel G. Bobrow
    - Douglas W. Clark
abstract: "List structures provide a general mechanism for representing easily changed structured data, but can introduce inefficiencies in the use of space when fields of uniform size are used to contain pointers to data and to link the structure. Empirically determined regularity can be exploited to provide more space-efficient encodings without losing the flexibility inherent in list structures. The basic scheme is to provide compact pointer fields big enough to accommodate most values that occur in them and to provide “escape” mechanisms for exceptional cases. Several examples of encoding designs are presented and evaluated, including two designs currently used in Lisp machines. Alternative escape mechanisms are described, and various questions of cost and implementation are discussed. In order to extrapolate our results to larger systems than those measured, we propose a model for the generation of list pointers and we test the model against data from two programs. We show that according to our model, list structures with compact cdr fields will, as address space grows, continue to be compacted well with a fixed-width small field. Our conclusion is that with a microcodable processor, about a factor of two gain in space efficiency for list structure can be had for little or no cost in processing time."
---

