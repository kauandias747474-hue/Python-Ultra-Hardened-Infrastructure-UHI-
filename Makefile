.PHONY: install test bench harden clean lint

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install ruff mypy pytest-asyncio pytest-benchmark bandit


test:
	pytest tests/ -v


bench:
	pytest tests/ --benchmark-only --benchmark-columns=min,max,mean,stddev

harden:
	ruff check .
	mypy .
	bandit -r .

audit:
	python 7-lab/disassembler/audit_bytecode.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf .ruff_cache
