.PHONY: test setup

test:
	coverage run manage.py test --settings=settings.test

setup:
	pipenv install -r
