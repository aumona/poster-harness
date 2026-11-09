.PHONY: all check clean
all:
	@mkdir -p output/pdf
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output/pdf main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output/pdf main.tex
check: all
	python3 scripts/check.py
clean:
	python3 scripts/clean.py
