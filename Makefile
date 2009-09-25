all: install test

install:
	@python setup.py install

test:
	@python src/specs/run_all_specs.py
