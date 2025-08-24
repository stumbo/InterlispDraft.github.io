---
title: "Chat _Streams_"
date: '1984-08-25'
authors: 
    - Acuff
    - Richard
abstract: "A chat stream is a connection between two processes oriented towards terminal service, but not necessarily restricted to that. A chat stream is inherently bi-directional so it is represented by two Interlisp-D streams; one each for input and output. The input stream is considered the primary handle on the connection and is used wherever operations are preformed that are not inherently only input or output. The following operations are available for chat streams (as well as the normal stream operations). In general these operations return true if the operation was successful, NIL if it could not be done:"
---

