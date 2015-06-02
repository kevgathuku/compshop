.PHONY: test

test:
	coverage run manage.py test --settings=settings.test
