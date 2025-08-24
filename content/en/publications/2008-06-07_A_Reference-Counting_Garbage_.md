---
title: "A Reference-Counting Garbage Collection Algorithm for Cyclical Functional Programming"
date: '2008-06-07'
authors: 
    - Baltasar Trancon y Widemann
abstract: "Reference-counting garbage collection is known to have problems with the collection of cyclically connected data. There are two historically significant styles of cycle-aware algorithms: The style of Brownbridge that maintains a subset of marked edges and the invariant that every cycle contains at least one marked edge, and the style of Martinez-Lins-Wachenchauzer (MLW) that involves local mark-and-scan procedures to detect cycles. The former is known to be difficult to design and implement correctly, and the latter to have pathological efficiency for a number of very typical situations. We present a novel algorithm that combines both approaches to obtain reasonably efficient local mark-and-scan phases with a marking invariant that is rather cheap to maintain. We demonstrate that the assumptions of this algorithm about mutator activity patterns make it well-suited, but not limited, to a functional programming technique for cyclic data. We evaluate the approach in comparison with simple and more sophisticated MLW algorithms using a simple benchmark based on that functional paradigm."
---

