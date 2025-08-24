---
title: "Impulse-86: A Substrate for Object-Oriented Interface Design"
date: '1986-11-01'
authors: 
    - Reid G. Smith
    - Rich Dinitz
    - Paul Barth
abstract: "Impulse-86 provides a general and extensible substrate upon which to construct a wide variety of interactive user interfaces for developing, maintaining, and using knowledge-based systems. The system is based on five major building blocks:               Editor, Editor Window, PropertyDisplay, Menu               , and               Operations               . These building blocks are interconnected via a uniform framework and each has a well-defined set of responsibilities in an interface.                                         Customized interfaces can be designed by declaratively replacing some of the building blocks in existing Impulse-86 templates. Customization may involve a wide range of activities, ranging from simple override of default values or methods that control primitive operations (               e.g.               , font selection), to override of more central Impulse-86 methods (               e.g.               , template instantiation). Most customized interfaces require some code to be written—to handle domain-specific commands. However, in all cases, the Impulse-86 substrate provides considerable leverage by taking care of the low-level details of screen, mouse, and keyboard manipulation.                          Impulse-86 is implemented in Strobe, a language that provides object-oriented programming support for Lisp. This simplifies customization and extension."
---

