.PHONY: clean start english german build-docker start-docker attach-to-docker

all: english

english: env/lib/python3.5/site-packages/spacy/data/en-1.1.0

german: env/lib/python3.5/site-packages/spacy/data/de-1.0.0

env/lib/python3.5/site-packages/spacy/data/en-1.1.0: env/bin/python
	env/bin/python -m spacy.en.download parser

env/lib/python3.5/site-packages/spacy/data/de-1.0.0: env/bin/python
	env/bin/python -m spacy.de.download parser

env/bin/python:
	virtualenv env -p python3.5 --no-site-packages
	env/bin/pip install --upgrade pip
	env/bin/pip install wheel
	env/bin/pip install -r requirements.txt
	env/bin/python setup.py develop

clean:
	rm -rfv bin develop-eggs dist downloads eggs env parts
	rm -fv .DS_Store .coverage .installed.cfg bootstrap.py
	rm -fv logs/*.txt
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;
	find . -depth -name '__pycache__' -exec rm -rfv {} \;
	sed -n '/^language: [a-z]\{2\}/!p' config/options.yml > tmp && mv tmp config/options.yml

build-docker: clean
	docker build -t jgontrum/spacyapi .

start-docker:
	mkdir -p /tmp/spacyapi-logs
	docker rm spacyapi || true
	docker run --name "spacyapi" -p "127.0.0.1:20040:20040" -v "/tmp/spacyapi-logs:/app/logs" jgontrum/spacyapi

attach-to-docker:
	 docker exec -i -t spacyapi /bin/bash 

start: env/bin/python
	env/bin/uwsgi --yaml=config/uwsgi.yml

