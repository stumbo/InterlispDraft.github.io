---
title: "The _Implementation_ of _Device-Independent Graphics Through Imagestreams_"
date: '1985-02-26'
authors: 
    - Jellinek
    - Herb
abstract: "The Interlisp-D system does all image creation through a set of functions and data structures for device-independent graphics, known popularly as DIG. DIG is achieved throught the use of a special flavor of stream, known as an imagestream. An imagestream, by convention, is any stream that has its IMAGEOPS field (described in detail below) set to a vector of meaningful graphical operations. Using imagestreams, we can write programs that draw and print on an output stream without regard to the underlying device, be it window, disk, Dover, 8044 or Diablo printers."
---

