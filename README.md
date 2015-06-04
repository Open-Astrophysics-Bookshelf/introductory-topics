# Notes for AST 208, "Planets and Telescopes"

These notes were written while teaching a sophomore-level astronomy course at Michigan State University. The background required is an introductory calculus sequence and a freshman-level physics course.

These notes are meant to supplement the course's main texts, Lissauer and de Pater (2013)  and Bennett et al. (2013).  The text layout uses the [`tufte-book`](https://tufte-latex.github.io/tufte-latex/) LaTeX class:  the main feature is a large right margin in which the students can take notes; this margin also holds small figures and sidenotes. Exercises are embedded throughout the text.  These range from ``reading exercises'' to longer, more challenging problems.  Because the exercises are spread throughout the text, there is a "List of Exercises" in the front matter to help with looking for specific problems.

## License

Except where explicitly noted, this work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

## Requirements for installing

0. Either pdfLaTeX or XeLaTeX.
1. [`tufte-book`](https://tufte-latex.github.io/tufte-latex/) LaTeX class
2. The [`starType`](https://github.com/nworbde/starType) macros.  You can install this from the source; alternatively, a shell script `install_local_starType` is provided to automatically fetch the macros into the directory of this package.
3. The `wasysym` package is used to generate astronomical symbols.
4. If you process the document with XeLaTeX, you will need either the TeX Gyre font family or the fonts Chaparral Pro, Source Code Pro, and Raleway Medium.

## To build

1. For a default installation, simply `make`.  This will build the document using pdfLaTeX.
2. If you wish to use XeLaTeX, change line 2 of the makefile to read `COMPILE=xelatex`

    1. If you have Chaparral Pro, Source Code Pro, and Raleway Medium fonts available, add the option `profonts` to the `\documentclass` directive in AST208-notes.tex.
    2. If you wish to use the STIX fonts for greek letters, add the option `stix` to the `\documentclass` directive in AST208-notes.tex.
