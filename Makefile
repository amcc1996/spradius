# Read code version
VERSION=$(shell cat ./VERSION)

# Data for communication with Github
GIT_BRANCH=$(shell git rev-parse --abbrev-ref HEAD)
TOKEN=$(shell cat ~/.github-access-token)
API_JSON=$(shell printf '{"tag_name": "v%s","target_commitish": "main","name": "v%s","body": "Release of version %s","draft": false,"prerelease": false}' $(VERSION) $(VERSION) $(VERSION))
URL=https://api.github.com/repos/amcc1996/spradius/releases

.PHONY: format coverage clean img tests deploy

lint:
	isort --check --color .
	black -l 79 --check .
	flake8 .

format:
	isort --color .
	black -l 79 .

coverage:
	pytest --cov-report html --cov spradius

clean:
	@rm -rf *.egg-info/
	@rm -rf build
	@rm -rf dist
	@rm -rf htmlcov
	@find . -name *__pycache__ -exec rm -rf {} +
	@rm -rf tests/results

benchmark:
	python3 ./tests/create_benchmark.py

tests:
	pytest

deploy: clean
	if [ "$(GIT_BRANCH)" != "main" ]; then echo "Not in main branch"; exit 1; fi
	curl -H "Authorization: token $(TOKEN)" --data '$(API_JSON)' $(URL)
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
