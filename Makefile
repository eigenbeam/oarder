.ONESHELL:
.PHONY: clean image lambda publish

oarder.zip: poetry.lock pyproject.toml oarder/*.py tests/*.py
	mkdir -p package
	poetry build
	poetry run pip install --upgrade -t package dist/*.whl
	cd package ; zip -r ../oarder.zip . -x '*.pyc'

clean:
	rm -f oarder.zip
	rm -rf package
	rm -rf dist

image: Dockerfile
	docker build -t oarder .

lambda: image
	docker create --name oarder-extract oarder
	docker cp oarder-extract:/usr/src/oarder/oarder.zip .
	docker rm oarder-extract

publish:
	aws s3 cp oarder.zip s3://oa-sbx-artifacts-9863/oarder.zip
