# Team Ergon AI — Automation Makefile
.PHONY: help check lesson1 c1 c2 c3 c4 c5 p2_c1 p2_c2 p2_c3 p2_c4 p2_c5 requirements clean

PYTHON = ./venv/Scripts/python.exe
PIP = ./venv/Scripts/pip.exe

help:
	@echo ====================================================
	@echo Team Ergon AI -- Automation Center
	@echo ====================================================
	@echo   make check        - Verify all libraries and stack status
	@echo   --- Phase 1 Challenges ---
	@echo   make c1 to c5     - Phase 1 Foundations Challenges
	@echo   --- Phase 2 Challenges (Files, JSON, Pydantic) ---
	@echo   make p2_c1        - Challenge 2.1 (Safe JSON File Writer)
	@echo   make p2_c2        - Challenge 2.2 (JSON File Loader)
	@echo   make p2_c3        - Challenge 2.3 (json.loads vs json.dumps)
	@echo   make p2_c4        - Challenge 2.4 (Pydantic Model Validation)
	@echo   make p2_c5        - Challenge 2.5 (End-to-End Ingestion Validator)
	@echo   make p2_c6        - Challenge 2.6 (Resilient API Client with requests)
	@echo   make p2_c7        - Challenge 2.7 (Tabular Data Analysis with pandas)
	@echo   make requirements - Freeze packages to requirements.txt
	@echo ====================================================

check:
	$(PYTHON) src/verify_stack.py

lesson1:
	$(PYTHON) challenges/01_variables.py

# Phase 1
c1:
	$(PYTHON) challenges/challenge_1.py
c2:
	$(PYTHON) challenges/challenge_2.py
c3:
	$(PYTHON) challenges/challenge_3.py
c4:
	$(PYTHON) challenges/challenge_4.py
c5:
	$(PYTHON) challenges/challenge_5.py

# Phase 2 (Files, JSON, Pydantic, Requests, Pandas)
p2_c1:
	$(PYTHON) challenges/p2_challenge_1.py
p2_c2:
	$(PYTHON) challenges/p2_challenge_2.py
p2_c3:
	$(PYTHON) challenges/p2_challenge_3.py
p2_c4:
	$(PYTHON) challenges/p2_challenge_4.py
p2_c5:
	$(PYTHON) challenges/p2_challenge_5.py
p2_c6:
	$(PYTHON) challenges/p2_challenge_6.py
p2_c7:
	$(PYTHON) challenges/p2_challenge_7.py

# Phase 3 (Ollama & Local LLM Client)
p3_c1:
	$(PYTHON) src/llm_client.py
llm:
	$(PYTHON) src/llm_client.py

requirements:
	$(PIP) freeze > requirements.txt
	@echo [+] requirements.txt successfully updated!
