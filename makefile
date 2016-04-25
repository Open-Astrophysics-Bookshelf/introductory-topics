BASE = AST208-notes
COMPILE = xelatex
OPS =  --file-line-error --synctex=1
RM = rm -f

CHAPTERS =	frontmatter \
			coordinates \
			light-telescopes \
			detection-exoplanets \
			beyond-kepler \
			resonance \
			planetary-atmospheres \
			constants-units \
			math-review \
			statistics

TEX_SRC = $(foreach chap, $(CHAPTERS), $(wildcard $(chap)/*.tex))

FIGURES =	frontmatter/cover-art.png \
			coordinates/figs/celestial-sphere.pdf \
			coordinates/figs/ecliptic.pdf \
			coordinates/figs/right-ascension.pdf \
			coordinates/figs/solar-day.pdf \
			coordinates/figs/parallax.pdf \
			coordinates/figs/angular-distance.pdf \
			coordinates/figs/angular-distance2.pdf \
			light-telescopes/figs/light-wave.pdf \
			light-telescopes/figs/diffraction.pdf \
			light-telescopes/figs/vector-addition.pdf \
			light-telescopes/figs/airmass.png \
			detection-exoplanets/figs/center-of-mass.pdf \
			detection-exoplanets/figs/elliptical-orbit.pdf \
			detection-exoplanets/figs/doppler.pdf \
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
			resonance/figs/simple-spring.png \
			resonance/figs/beats.pdf \
			resonance/figs/damped.pdf \
			resonance/figs/damped-driven.pdf \
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

$(BASE).pdf: $(BASE).tex $(TEX_SRC) $(BIBS) $(FIGURES)
	git rev-parse --short=8 HEAD > git-info.tex
	$(COMPILE) $(OPS) $(BASE).tex
	bibtex AST208-notes.aux
	$(COMPILE) $(OPS) $(BASE).tex
	$(COMPILE) $(OPS) $(BASE).tex

clean:
	$(RM) *.aux *.log *.dvi *.bbl *.blg *.toc *.lof *.log *.synctex* *.out

realclean: clean
	$(RM) $(BASE).pdf
