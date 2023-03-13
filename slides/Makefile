figs = 
nom = demo

view : ${nom}.pdf
	atril ${nom}.pdf

${nom}.pdf : ${nom}.tex ${figs} ${nom}.aux
	pdflatex ${nom}.tex

${nom}.aux :
	pdflatex ${nom}.tex

clean :
	rm -f *.dvi *.aux *.log *.blg *.bbl *.nav *.snm *.toc *.out \
	*.pdftex* *.pdftex* \
	dvips.pdf landscape.pdf resize.pdf ${nom}.pdf ${nom}.ps