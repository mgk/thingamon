build: clean
	python setup.py sdist bdist_wheel

clean:
	$(RM) -fr build dist *.egg-info .coverage htmlcov

very-clean: clean
	find . -name '*.pyc' | xargs rm -f

install:
	pip install -r requirements.txt
	pip install -r requirements-test.txt

install-dev: install
	pip install -r requirements-dev.txt

release: clean test
	python setup.py sdist bdist_wheel
	twine upload -r pypitest dist/*
	git push origin master --tags
	@echo
	@echo "so far so good..."
	@echo "wait for Travis green light, then:"
	@echo
	@echo "twine upload dist/*"
	@echo
	@echo "do bump-minor or bump-patch before next release"

test:
	@pycodestyle thingamon
	@tox

coverage:
	coverage run --source=thingamon -m py.test
	coverage html

.PHONY: build clean very-clean install install-dev release test coverage
