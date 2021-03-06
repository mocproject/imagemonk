# ImageMonk makefile

# You can set these variables from the command line
PROJECT = imagemonk

.PHONY: help
# Put it first so that "make" without argument is like "make help"
# Adapted from:
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## List Makefile targets
	$(info Makefile documentation)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

clean-tox:
	rm --recursive --force ./.mypy_cache
	rm --recursive --force ./.tox
	rm --force .coverage
	find ./tests -type d -name __pycache__ -prune -exec rm --recursive --force {} \;

clean-py:
	rm --recursive --force ./dist
	rm --recursive --force ./build
	rm --recursive --force ./*.egg-info
	find ./$(PROJECT) -type d -name __pycache__ -prune -exec rm --recursive --force {} \;

clean-docs:
	rm --recursive --force docs/_build
	rm --force docs/$(PROJECT)*.rst
	rm --force docs/modules.rst

clean: clean-tox clean-py clean-docs; ## Clean temp build/cache files and directories

wheel: ## Build Python binary distribution wheel package
	poetry build --format wheel

source: ## Build Python source distribution package
	poetry build --format sdist

test: clean-tox ## Run the project testsuite(s)
	tox

publish: clean test wheel source ## Build and upload to pypi (requires $PYPI_API_KEY be set)
	@poetry publish --username __token__ --password $(PYPI_API_KEY)

docs: clean-docs ## Build the documentation using Sphinx
	tox -e docs
