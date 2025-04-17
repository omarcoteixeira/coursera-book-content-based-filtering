.PHONY: install
install:
	./tools/local/bin/install_dependencies.sh

.PHONY: install-test
install-test:
	pip install -r requirements_tests.txt;

.PHONY: up
up:
	./tools/local/bin/run_airflow.sh

.PHONY: cleanup
cleanup:
	./tools/local/bin/cleanup.sh

.PHONY: test
test:
	python -m pytest tests;

.PHONY: lint
lint:
	pylint --recursive=y dags;