.PHONY: test validate

test:
	python3 -m unittest discover -s tests -v

validate: test
	python3 scripts/validate_release.py
