VENV=venv/bin/activate

INPUT=inputs/20200720-hxl-tags-atts.csv
MODEL=working/compiled-model.json

build: $(VENV) $(MODEL)

run: build
	. $(VENV) && python -m hxltags.lookup $(MODEL)

$(MODEL): $(INPUT)
	mkdir -p working
	. $(VENV) && python -m hxltags.compiler $(INPUT) > $(MODEL)

$(VENV): requirements.txt
	rm -rf venv
	python3 -m venv venv
	. $(VENV) && pip install -r requirements.txt
