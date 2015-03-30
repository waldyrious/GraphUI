# GraphUI

A python-based visual [graph](https://en.wikipedia.org/wiki/Graph_%28mathematics%29) editor.
It can create and edit [GraphViz](http://www.graphviz.org/) files
specified in the [DOT language](https://en.wikipedia.org/wiki/DOT_%28graph_description_language%29).

This is a fork of the **[GraphUI utility](https://code.google.com/p/enough/wiki/Graphui)**
from the [Enough project](https://code.google.com/p/enough/),
originally developed by [Noam Lewis](https://github.com/sinelaw)
and [Eyal Lotem](https://github.com/Peaker), but abandoned since 2007.

This repository was automatically exported from code.google.com/p/enough
using the [Google Code Github Exporter](https://code.google.com/export-to-github/).

Below are the contents of the [Graphui page](https://code.google.com/p/enough/wiki/Graphui)
from the original Enough wiki:

----

## Status
We have re-implemented the [PackageLibrary](PackageLibrary.md) - so now we need a major re-write of Graphui as well.

## Download
The latest version (BEFORE the anticipated rewrite) is:
[Latest Version](http://enough.googlecode.com/files/graphui488_only.tar.gz)

## Features
Graphui (pronounced grafoo-ee) is an attempt at a generic graph editing gui. The code is in the svn under [graphui](http://enough.googlecode.com/svn/trunk/graphui/).

Short **[Demo video](http://www.youtube.com/watch?v=RT87JfTYIvo)**

Screenshot:

![screenshot](http://i.imgur.com/Vz30UsQ.jpg)

Here are the current "features":
  * Automatic layout using [Dot, Neato & Twopi](http://www.graphviz.org) (Graphviz).
    You can switch layout engines in real time
  * Cross-platform - tested on Linux (ubuntu) and Windows
  * Save and load graphs
  * Connect, disconnect, add and remove nodes
  * Zoom & pan
  * Stretch or keep DOT's aspect ratio
  * Undo/redo
  * Multi-line text labels for nodes and edges
  * Record animation - makes a series of BMP files you can later turn into a video
    using `videowriter` or some other tool.
  * All changes are animated to make it easy to see what is changing (and to make it cooler!)

More coming soon!

**Requirements**: [Python](http://www.python.org) 2.5, [Pygame](http://www.pygame.org), [Twisted](http://www.twistedmatrix.com), and [Graphviz](http://www.graphviz.org) (aka dot). On Windows you will need also [pywin32](http://sourceforge.net/projects/pywin32/).

For better performance get Pyrex too (and run setup.py build make sure to use the .so files).

Here is a short animation showing Graphui switching between layout engines:

![graphui switching layouts](http://i.imgur.com/Vz30UsQ.jpg)

## Applications
Graphui is still under development. Here are some ideas for applications.
  * Diagram editor - the simplest most obvious application. Use Graphui instead of manual-layout programs (such as Visio and Dia) to easily create flow charts, state machine diagrams, etc.
  * Graph visualization - because Graphui's format is simply pickled Python objects, you can easily create tools that make graphs from any dataset and then view/edit the graph in Graphui.
  * Graph algorithms demonstration and visualization - a researcher/student may easily extend Graphui's code to work on graph algorithms in a live environment, instead of iterating between running his algorithm test program and viewing the result seperately.

### Future applications
Graphui may be suitable for testing a [Live programming](LiveProgramming.md) environment. We will have to add features for viewing the code in different ways (not just as a Dot graph), especially as a compact tree (like the one used in graphical file managers to represent the directory tree).
