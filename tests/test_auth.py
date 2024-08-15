import sys
import os

# Adiciona o diretório "app" ao caminho de pesquisa do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Agora você pode importar a função login_autenticacao
from auth import login_autenticacao

def test_auth():
    assert login_autenticacao("user", "pass", 1) == True
