.PHONY: sdist test lint uv-test uv-easy-test

sdist:
	python setup.py sdist

test:
	pytest -v -s --cov=chop_doc --cov-report=term-missing tests

lint:
	black .

uv-test:
	uv run pytest tests

uv-easy-test:
	uv run test_main.py