---
title: "A Selective Undo Mechanism for Graphical User Interfaces Based on Command Objects"
date: '1994-09-01'
authors: 
    - Thomas Berlage
abstract: "It is important to provide a recovery operation for applications with a graphical user interface. A restricted linear undo mechanism can conveniently be implemented using object-oriented techniques. Although linear undo provides an arbitrarily long history, it is not possible to undo isolated commands from the history without undoing all following commands. Various undo models have been proposed to overcome this limitation, but they all ignore the problem that in graphical user interfaces a previous user action might not have a sensible interpretation in another state. Selective undo introduced here can undo isolated commands by copying them into the current state “if that is meaningful.” Furthermore, the semantics of selective undo are argued to be more natural for the user, because the mechanism only looks at the command to undo and the current state and does not depend on the history in between. The user interface for selective undo can also be implemented generically. Such a generic implementation is able to provide a consistent recovery mechanism in arbitrary applications."
---

