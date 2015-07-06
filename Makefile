.PHONY: test

test:
	coverage run manage.py test --settings=settings.test

setup:
	pip install -r requirements.txt
	pip install -r requirements/local.txt
