---
title: "Extending Object Oriented Programming in _Smalltalk_"
date: '1980-08-25'
authors: 
    - Ira P. Goldstein
    - Daniel G. Bobrow
abstract: "Smalltalk is an object oriented programming language with behavior invoked by passing messages between objects. Objects with similar behavior are grouped into classes. These classes form a hierarchy. When an object receives a message, the class or one of its superclasses provides the corresponding method to be executed. We have built an experimental Personal Information Environment (PIE) in Smalltalk that extends this paradigm in several ways. A PIE object, called a node, can have multiple perspectives, each of which provides independent specialized behaviors for the object as a whole, thus providing multiple inheritance for nodes. Nodes have metadescription to guide viewing of the objects during browsing, provide default values, constrain the values of attributes, and define procedures to be run when values are sought or set. All nodes have unique names which allow objects to migrate between users and machines. Finally attribute lookup for nodes is context sensitive, thereby allowing alternative descriptions to be created and manipulated. This paper first reviews Smalltalk, then discusses our implementation of each of the above capabilities within PIE, a Smalltalk system for representing and manipulating designs. We then describe our experience with PIE applied to software development and technical writing. Our conclusion is that the resulting hybrid is a viable offspring for exploring design problems."
---

