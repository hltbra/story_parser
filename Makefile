all: install test

install:
	@python setup.py install

test:
	@python src/specs/parsing_valid_stories.py
	@python src/specs/parsing_invalid_stories.py
	@python src/specs/regex_with_i18n.py && echo 'Ran doctest OK!' || echo 'Ran doctest FAIL'
