BASE = planets-notes
TEX = pdflatex
BIB = bibtex
OPS =  --file-line-error --synctex=1
COMPILE = $(TEX) $(OPS)
RM = rm -f

CHAPTERS =	frontmatter \
			coordinates \
			light-telescopes \
			spectroscopy \
			detection-exoplanets \
			beyond-kepler \
			planetary-atmospheres \
			constants-units \
			math-review \
			statistics

TEX_SRC = $(foreach chap, $(CHAPTERS), $(wildcard $(chap)/*.tex))
HANDOUTS = 	coordinates-handout.pdf \
			light-telescopes-handout.pdf \
			spectroscopy-handout.pdf \
			detection-exoplanets-handout.pdf \
			beyond-kepler-handout.pdf \
			planetary-atmospheres-handout.pdf \
			constants-units-handout.pdf \
			math-review-handout.pdf \
			statistics-handout.pdf

FIGURES =	frontmatter/cover-art.png \
			coordinates/figs/celestial-sphere.pdf \
			coordinates/figs/ecliptic.pdf \
			coordinates/figs/right-ascension.pdf \
			coordinates/figs/solar-day.pdf \
			coordinates/figs/parallax.pdf \
			coordinates/figs/angular-distance.pdf \
			coordinates/figs/angular-distance2.pdf \
			light-telescopes/figs/light-wave.pdf \
			light-telescopes/figs/magnification-in-water.pdf \
			light-telescopes/figs/reflection-and-snell-AST208.pdf \
			light-telescopes/figs/diffraction.pdf \
			light-telescopes/figs/vector-addition.pdf \
			light-telescopes/figs/airmass.png \
			spectroscopy/figs/doppler.pdf \
			spectroscopy/figs/H-spectrum.pdf \
			spectroscopy/figs/slit-and-grating.pdf \
			spectroscopy/figs/diffraction-grating.pdf \
			spectroscopy/figs/cd-diffraction-AST208.pdf \
			detection-exoplanets/figs/center-of-mass.pdf \
			detection-exoplanets/figs/elliptical-orbit.pdf \
			detection-exoplanets/figs/orbital-inclination.pdf \
			detection-exoplanets/figs/transit.pdf \
			detection-exoplanets/figs/inclination-probability.pdf \
			beyond-kepler/figs/polar-coordinates.pdf \
			beyond-kepler/figs/change-polar-unit-vectors.pdf \
			beyond-kepler/figs/coriolis-exercise.pdf \
			beyond-kepler/figs/Roche.pdf \
			beyond-kepler/figs/Tides.pdf \
			beyond-kepler/figs/Earth-Moon-tides.pdf \
			beyond-kepler/figs/lunar-tidal-force.pdf \
			beyond-kepler/figs/tidal-torque.pdf \
			beyond-kepler/figs/Inertia.png \
			planetary-atmospheres/figs/hydrostatic-equilibrium.pdf \
			planetary-atmospheres/figs/column.pdf \
			planetary-atmospheres/figs/beta-plane.pdf \
			planetary-atmospheres/figs/cyclone.pdf \
			math-review/figs/high-school-triangle.pdf \
			math-review/figs/trig-schematic.pdf \
			math-review/figs/trig-addition.pdf \
			statistics/figs/set-1.pdf \
			statistics/figs/set-2.pdf \
			statistics/figs/set-3.pdf \
			statistics/figs/set-4.pdf \
			statistics/figs/Poisson.pdf \
			statistics/figs/Normal_sigma1.pdf \
			statistics/figs/Normal_mu0.pdf \
			statistics/figs/sigma.pdf

BIBS = bibs/ast208.bib

default = $(BASE).pdf

$(BASE).pdf: $(BASE).tex $(TEX_SRC) $(BIBS) $(FIGURES)
	git rev-parse --short=8 HEAD > git-info.tex
	$(COMPILE) $(BASE).tex
	$(BIB) $(BASE).aux
	$(COMPILE) $(BASE).tex
	$(COMPILE) $(BASE).tex
	$(COMPILE) $(BASE).tex

coordinates-handout.pdf: coordinates-handout.tex $(TEX_SRC) $(FIGURES)
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

light-telescopes-handout.pdf: light-telescopes-handout.tex $(TEX_SRC) $(BIBS) $(FIGURES)
	$(COMPILE) $<
	$(BIB) light-telescopes-handout.aux
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<
		
spectroscopy-handout.pdf: spectroscopy-handout.tex $(TEX_SRC) $(FIGURES)
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

detection-exoplanets-handout.pdf: detection-exoplanets-handout.tex $(TEX_SRC) $(FIGURES)
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

beyond-kepler-handout.pdf: beyond-kepler-handout.tex $(TEX_SRC) $(FIGURES)
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

planetary-atmospheres-handout.pdf: planetary-atmospheres-handout.tex $(TEX_SRC) $(BIBS) $(FIGURES)
	$(COMPILE) $<
	$(BIB) planetary-atmospheres-handout.aux
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

constants-units-handout.pdf: constants-units-handout.tex $(TEX_SRC)
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

math-review-handout.pdf: math-review-handout.tex $(TEX_SRC) $(FIGURES)
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

statistics-handout.pdf: statistics-handout.tex $(TEX_SRC) $(BIBS) $(FIGURES)
	$(COMPILE) $<
	$(BIB) statistics-handout.aux
	$(COMPILE) $<
	$(COMPILE) $<
	$(COMPILE) $<

handouts: $(HANDOUTS)

clean:
	$(RM) *.aux *.log *.dvi *.bbl *.blg *.toc *.lof *.loe *.log *.synctex* *.out

realclean: clean
	$(RM) $(BASE).pdf *-handout.pdf
