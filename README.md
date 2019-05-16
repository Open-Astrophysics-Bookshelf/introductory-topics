# Introductory Topics in Astronomy: Planets and Telescopes

Part of the [Open Astrophysics Bookshelf](http://open-astrophysics-bookshelf.github.io/).  A pdf of these notes is available at [this link](http://www.pa.msu.edu/~ebrown/docs/AST208-notez.pdf).

These notes were written while teaching (and revamping) a one-semester introductory astronomy course, "Planets and Telescopes" at Michigan State University. The background required was an introductory calculus sequence and first-year physics. The reason for the odd juxtaposition of topics&mdash;planets and telescope&mdash;is that the course was created from the merger of two undergraduate courses, one of which was a laboratory course with observing done at the campus observatory.

These notes were meant to supplement the course's main texts, Ryden and Peterson, _Foundations of Astrophysics_, and Taylor, _An Introduction to Error Analysis_. The text layout uses the [`tufte-book`](https://tufte-latex.github.io/tufte-latex/) LaTeX class:  the main feature is a large right margin in which the students can take notes; this margin also holds small figures and sidenotes. Exercises are embedded throughout the text. These range from reading exercises to longer, more challenging problems. Because the exercises are spread throughout the text, there is a "List of Exercises" in the front matter to help with looking for specific problems. There are further notes and exercises on statistics in the form of [Jupyter notebooks](http://jupyter.org) in the folder `statistics/notebooks`.

Because the course structure is idiosyncratic to Michigan State University, I've also added the chapters as individual handouts (files `*-handout.tex`). These can be rebuilt by running `python make_handous.py`; you may need to adjust by hand the placement of figures.

## License

Except where explicitly noted, this work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

## Requirements for installing

0. Either pdfLaTeX or XeLaTeX.
1. [`tufte-book`](https://tufte-latex.github.io/tufte-latex/) LaTeX class
2. The [`starType`](https://github.com/nworbde/starType) macros.  You can install this from the source; alternatively, a shell script `install_local_starType` is provided to automatically fetch the macros into the directory of this package.
3. The `wasysym` package is used to generate astronomical symbols.
4. An up-to-date version (5.8 or later) of the `fontawesome5` LaTeX class; if you are using XeLaTeX, you will need to install the fontawesome otf glyphs as well. (Alternatively, you can redefine the `\notebook` command, defined in `planets-notes.tex` and in handout script `make_handouts.py`, to a standard LaTeX symbol.)
4. If you process the document with XeLaTeX, you will need either the TeX Gyre font family or the fonts Chaparral Pro, Source Code Pro, and Raleway Medium.

## To build

1. For a default installation, simply `make`.  This will build the document using pdfLaTeX.

2. The default TeX engine is pdfLaTeX; if you wish to use XeLaTeX, change line 2 of the makefile to read `COMPILE=xelatex`

    1. If you have Chaparral Pro, Source Code Pro, and Raleway Medium fonts available, add the option `profonts` to the `\documentclass` directive in AST208-notes.tex.
    2. If you wish to use the STIX fonts for greek letters, add the option `stix` to the `\documentclass` directive in AST208-notes.tex.

3. To build the handouts, at the command line type `make handouts`.
