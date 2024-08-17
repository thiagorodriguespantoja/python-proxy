from auth.auth import autenticar_usuario  # Certifique-se de que o caminho seja correto

def test_autenticacao():
    usuario = "14ad9a9ccd37c"
    senha = "996f9e5a18"
    resultado = autenticar_usuario(usuario, senha)
    assert resultado is True
