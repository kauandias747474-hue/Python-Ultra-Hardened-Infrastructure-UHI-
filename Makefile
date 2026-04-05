.PHONY: install test bench harden clean lint

# Instalação profissional de dependências
install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install ruff mypy pytest-asyncio pytest-benchmark bandit

# Executa a suíte de testes assíncronos
test:
	pytest tests/ -v

# Executa o benchmark de performance (Latência e Jitter)
bench:
	pytest tests/ --benchmark-only --benchmark-columns=min,max,mean,stddev

# Executa o "Hardening Check" (Linter + Tipagem + Segurança)
harden:
	ruff check .
	mypy .
	bandit -r .

# Auditoria de Bytecode (Módulo 7-Lab)
audit:
	python 7-lab/disassembler/audit_bytecode.py

# Limpa arquivos temporários de cache
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf .ruff_cache
