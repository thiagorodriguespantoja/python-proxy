from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_navegador():
    # Inicializando o navegador com o ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executa o navegador no modo headless (sem interface)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return navegador

navegador = iniciar_navegador()

# Exemplo de uso: Acessar o Instagram
try:
    navegador.get("https://www.instagram.com")
    print(f"Autenticando no Instagram...")

    # Validação do título da página para garantir que o Instagram foi carregado
    if "Instagram" in navegador.title:
        print("Página do Instagram carregada com sucesso!")
    else:
        print("Falha ao carregar a página do Instagram.")

    # Captura de tela (printscreen) após carregar o Instagram
    screenshot_filename = 'screenshot_instagram.png'
    navegador.save_screenshot(screenshot_filename)
    print(f"Screenshot salvo como {screenshot_filename}")

except Exception as e:
    print(f"Erro durante o login: {e}")
finally:
    navegador.quit()



