# verify_stack.py — Team Ergon System Check
import sys

# Ensure Windows terminal handles UTF-8 cleanly
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import chromadb
import pydantic
import requests
import ollama
import pandas as pd
import streamlit as st
import lightgbm as lgb
import sklearn

print("\n" + "=" * 52)
print("[*] TEAM ERGON BACKEND STATUS: ALL SYSTEMS ONLINE")
print("=" * 52)
print(f"[+] ChromaDB (Vector DB)     : v{chromadb.__version__}")
print(f"[+] Pydantic (Schema Guard)   : v{pydantic.__version__}")
print(f"[+] Requests (API Telephone)  : v{requests.__version__}")
print(f"[+] Ollama (Python Client)    : Ready")
print(f"[+] Pandas (Data Science)     : v{pd.__version__}")
print(f"[+] Streamlit (UI Engine)     : v{st.__version__}")
print(f"[+] LightGBM (ML Fallback)    : v{lgb.__version__}")
print(f"[+] Scikit-Learn (ML Core)    : v{sklearn.__version__}")
print("=" * 52)
print("[+] CONGRATULATIONS! Your AI sandbox is 100% ready.\n")
