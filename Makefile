.ONESHELL:
.PHONY: clean lambda

oarder.zip: poetry.lock pyproject.toml oarder/*.py tests/*.py
	mkdir -p package
	poetry build
	poetry run pip install --upgrade -t package dist/*.whl
	cd package ; zip -r ../oarder.zip . -x '*.pyc'

clean:
	rm -f oarder.zip
	rm -rf package
	rm -rf dist

lambda: Dockerfile
	docker build -t oarder .

