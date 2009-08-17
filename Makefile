all: install test

install:
	@python setup.py install

test:
	@python src/tests/parsing_valid_stories.py
	@python src/tests/parsing_invalid_stories.py
	@python src/tests/regex_with_i18n.py && echo 'Ran doctest OK!' || echo 'Ran doctest FAIL'
