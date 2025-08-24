---
title: "Finite State Machine Data Storage Where Data Transition Is Accomplished without the Use of Pointers"
date: '1995-09-12'
authors: 
    - Ronald M. Kaplan
    - Martin Kay
    - John Maxwell
abstract: "An FSM data structure is encoded by generating a transition unit of data corresponding to each transition which leads ultimately to a final state of the FSM. Information about the states is included in the transition units, so that the encoded data structure can be written without state units of data. The incoming transition units to a final state each contain an indication of finality. The incoming transition units to a state which has no outgoing transition units each contain a branch ending indication. The outgoing transition units of each state are ordered into a comparison sequence for comparison with a received element, and all but the last outgoing transition unit contain an alternative indication of a subsequent alternative outgoing transition. The indications are incorporated with the label of each transition unit into a single byte, and the remaining byte values are allocated among a number of pointer data units, some of which begin full length pointers and some of which begin pointer indexes to tables where pointers are entered. The pointers may be used where a state has a large number of incoming transitions or where the block of transition units depending from a state is broken down to speed access. The first outgoing transition unit of a state is positioned immediately after one of the incoming transitions so that it may be found without a pointer. Each alternative outgoing transition unit is stored immediately after the block beginning with the previous outgoing transition unit so that it may be found by proceeding through the transition units until the number of alternative bits and the number of branch ending bits balance."
---

