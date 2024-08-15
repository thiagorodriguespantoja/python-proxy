import sys
import os

# Adiciona o caminho absoluto para o diretório 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Importe a função login_autenticacao do auth.py no diretório app
from auth import login_autenticacao

def test_auth():
    assert login_autenticacao("user", "pass", 1) == True
