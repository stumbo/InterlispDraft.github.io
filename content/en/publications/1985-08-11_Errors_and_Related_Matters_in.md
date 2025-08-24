---
title: "Errors and Related Matters in _CommonLoops_ - _A Proposal_"
date: '1985-08-11'
authors: 
    - Thompson
    - Henry
abstract: "This proposal represents an attempt to provide a set of control primatives for CommonLoops which will 1) Support the existing Interlisp error handling mechanisms (including ERROR and friends, ERRORSET and friends, RESETLST and friends, ERRORTYPELST, BREAKCHECK and its consequences, and the relationships between ERRORX, FAULT1 and BREAK1, all in the context of spaghetti stacks and the existing process mechanisms; 2) Support the CommonLisp constructs catch, throw, unwindprotect, the relationship of unwindprotect to go and return(-from), error, cerror and warn; 3) Substantially reproduce the functionality of the ZetaLisp signalling facility; 4) Be a reasonably plausible attempt to take the high ground wrt whatever proposals the CommonLisp working party on error handling come up with; 5) Be a Good Thing in its own right."
---

