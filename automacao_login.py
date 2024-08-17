from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_navegador():
    # Inicializando o navegador com o ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executa o navegador no modo headless (sem interface)
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return navegador

navegador = iniciar_navegador()

# Exemplo de uso: Acessar o Instagram com o proxy configurado
try:
    navegador.get("https://www.instagram.com")
    print(f"Autenticando no Instagram...")

    # Captura de tela (printscreen) após carregar o Instagram
    screenshot_filename = 'screenshot_instagram.png'
    navegador.save_screenshot(screenshot_filename)
    print(f"Screenshot salvo como {screenshot_filename}")
except Exception as e:
    print(f"Erro durante o login: {e}")
finally:
    navegador.quit()


