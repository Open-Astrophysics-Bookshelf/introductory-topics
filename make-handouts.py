"""
Generates files <chapter>-handout.tex that can then be processed to make 
handouts. Adjust the string `frontmatter` to make the fonts to your liking.
"""

frontmatter=r'''\documentclass[handout]{astro-bookshelf}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=black,urlcolor=blue}

\usepackage{wasysym}

\graphicspath{{frontmatter/}{coordinates/figs/}{light-telescopes/figs/}{spectroscopy/figs/}{detection-exoplanets/figs/}{beyond-kepler/figs/}{planetary-atmospheres/figs/}{constants-units/figs/}{math-review/figs/}{statistics/figs/}}

\setcounter{secnumdepth}{1}

\usepackage[units,derivatives,vectors,code,symbols]{starType}
\input{symbols}
\newcommand{\newterm}[1]{\textsc{#1}}

\author{Edward Brown}
\publisher{Open Astrophysics Bookshelf}
\date{9 May 2018}
'''

backmatter=r'''
\bibliographystyle{plainnat}
\bibliography{bibs/AST208}

\end{document}
'''

titles = {
	"coordinates":"Coordinates: Specifying Locations on the Sky",
    "light-telescopes":"Light and Telescopes",
	"spectroscopy":"Spectroscopy",
    "detection-exoplanets":"Detection of Exoplanets",
    "beyond-kepler":"Beyond Kepler's Laws",
    "planetary-atmospheres":"Planetary Atmospheres",
    "constants-units":"Constants and Units",
    "math-review":"Mathematics Review",
    "statistics":"Probability and Statistics"
}

# execution starts here

for chapter in titles:
    texfile=chapter.strip()+'-handout.tex'

    title = r'\title{{{0}}}'.format(titles[chapter])
    chapter = r'\input{{{0}/{0}}}'.format(chapter)
    folios =\
        (frontmatter,title,r'\begin{document}',r'\maketitle',chapter,backmatter)

    with open(texfile,'w') as f:
        f.write('\n\n'.join(folios))
