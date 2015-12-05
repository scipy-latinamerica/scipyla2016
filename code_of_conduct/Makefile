build: en pt es

en: coc_en.html

pt: coc_pt.html

es: coc_es.html

%.html: %.md
	pandoc -f markdown -t html -o $@ $<

clean:
	rm -rf *.html
