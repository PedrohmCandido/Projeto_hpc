#!/usr/bin/env bash
set -e

# Ative seu venv antes, se desejar:
# python3 -m venv .venv && source .venv/bin/activate

echo "[build] Instalando dependências..."
pip install -r env/requirements.txt

echo "[build] OK"
