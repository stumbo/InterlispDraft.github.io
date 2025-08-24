---
title: "A Processor for a High-Performance Personal Computer"
date: '1998-08-01'
authors: 
    - Butler W. Lampson
    - Kenneth A. Pier
abstract: "This paper describes the design goals, micro-architecture. and implementation of the microprogrammed processor for a compact high-performance personal computer. This computer supports a range of high-level language environments and high bandwidth I/O devices. Besides the processor. it has a cache, a memory map, main storage. and an instruction fetch unit; these are described in other papers. The processor can be shared among 16 microcode tasks, performing microcode context switches on-demand with essentially no overhead. Conditional branches are done without any lookahead or delay. Micro-instructions are fairly tightly encoded and use an interesting variant on control field sharing. The processor implements a large number of internal registers. hardware stacks. acyclic shifter/masker, and an arithmetic/logic unit, together with external data paths for instruction fetching, memory interface, and I/O. in a compact, pipe-lined organization. The machine has a 50 ns microcycle, and can execute a simple macroinstruction in one cycle; the available I/O bandwidth is 640 Mbits/sec. The entire machine. including disk, display and network interfaces, is implemented with approximately 3000 NISI components, mostly EC:. 10K; the processor is about 35% of this. In addition, there are up to 4 storage modules, each with about 300 16K or 64K RAMS and 200 nisi components, for a total of 8 Mbytes. Several prototypes are currently running."
---

