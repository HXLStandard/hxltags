VENV=venv/bin/activate
NLTK_DATA=venv/nltk_data

run: $(VENV)
	. $(VENV) && python tag-prediction.py

$(VENV): requirements.txt
	rm -rf venv
	python3 -m venv venv
	. $(VENV) && pip install -r requirements.txt
	NLTK_DATA=$(NLTK_DATA) . $(VENV) && python -m textblob.download_corpora lite
