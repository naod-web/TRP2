# Makefile

.PHONY: setup test clean spec-check

setup:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v --tb=short

test-docker:
	@echo "Dockerfile not used; run in MCP server."

clean:
	rm -rf __pycache__ *.pyc .pytest_cache

spec-check:
	@echo "Manual spec alignment check not automated yet."
	@echo "TODO: implement basic static check against specs/*.md"
