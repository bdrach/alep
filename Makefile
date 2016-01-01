# This is the makefile for building the ALEP website.

RST = draft/
TEMPLATES = build/templates/
STATIC = draft/static/
PDF_OUTPUT = draft/static/pdfs/
DEST = _html/

GITHUB_REPO_URL = "https://github.com/bdrach/alep.git"

all: local

clean:
	rm -rf $(DEST)

directories:
	mkdir -p $(DEST)
	rsync -a --exclude='*.xcf' $(STATIC) $(DEST)static/

# builds site with root directory configured for reading files in browser locally
local: clean directories
	python build/build_site.py --local $(RST) $(TEMPLATES) $(DEST)

# builds site with correct root directory ('/') for running on webserver
server: clean directories
	python build/build_site.py $(RST) $(TEMPLATES) $(DEST)

upload: server
	git checkout gh-pages
	rm -rf alep-website
	rm -rf alep-website/labs/ alep-website/static/ *.html
	cp -r _html/* ./
	git add labs/* alep-website/* *.html
	git commit -a -m "Site Update"
	git push
	git checkout master

show:
	cd $(DEST)
	python -m SimpleHTTPServer

# creates pdf versions of all labs
lab-pdf:
	mkdir -p $(PDF_OUTPUT)
	mkdir _html_for_pdfgen/
	python build/build.py --local $(RST) $(TEMPLATES) _html_for_pdfgen/
	cp -r $(STATIC) _html_for_pdfgen/
	for filename in _html_for_pdfgen/labs/*.html; \
	do \
		basename=$$(basename "$$filename"); \
		name="$${basename%.*}"; \
		echo $(PDF_OUTPUT)/labs/"$$name"".pdf"; \
		wkhtmltopdf \
			--zoom .8 \
			--page-size Letter \
			--footer-center [page] \
			--footer-font-name Times \
			--footer-spacing 15 \
			-B 35mm -T 25mm -L 10mm -R 10mm \
			--disable-internal-links --disable-external-links \
			--javascript-delay 10000 \
			"$$filename" $(PDF_OUTPUT)/"$$name"".pdf"; \
	done;
