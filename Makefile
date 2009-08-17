all: test

test:
	@python parsing_valid_stories.py
	@python parsing_invalid_stories.py
	@python regex_with_i18n.py && echo 'Ran doctest OK!' || echo 'Ran doctest FAIL'
