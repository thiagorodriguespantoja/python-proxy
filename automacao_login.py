import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Cria a pasta para armazenar os logs e screenshots
os.makedirs("output", exist_ok=True)

# Configurar o logging para armazenar os logs na pasta 'output'
log_filename = 'output/selenium_logs.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def iniciar_navegador():
    # Inicializando o navegador com o ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executa o navegador no modo headless (sem interface)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    logging.info("Navegador iniciado com sucesso.")
    return navegador

def autenticar_instagram(navegador):
    try:
        navegador.get("https://www.instagram.com")
        logging.info("Página do Instagram carregada com sucesso.")
        print(f"Autenticando no Instagram...")

        # Validação do título da página para garantir que o Instagram foi carregado
        if "Instagram" in navegador.title:
            logging.info("Página do Instagram carregada com sucesso!")
            print("Página do Instagram carregada com sucesso!")
        else:
            logging.error("Falha ao carregar a página do Instagram.")
            print("Falha ao carregar a página do Instagram.")

        # Captura de tela (printscreen) após carregar o Instagram
        screenshot_filename = 'output/screenshot_instagram.png'
        navegador.save_screenshot(screenshot_filename)
        logging.info(f"Screenshot salvo como {screenshot_filename}. Verifique a imagem para garantir que a página foi carregada corretamente.")
        print(f"Screenshot salvo como {screenshot_filename}. Verifique a imagem para garantir que a página foi carregada corretamente.")

        # Verificar se a página foi carregada com sucesso
        try:
            elemento_login = navegador.find_element(By.NAME, 'username')
            logging.info("Campo de login encontrado com sucesso!")
            print("Campo de login encontrado com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao encontrar o campo de login: {e}")
            print(f"Erro ao encontrar o campo de login: {e}")

        # Interação com a página, como inserir dados de login
        try:
            elemento_login.send_keys("meu_usuario")
            elemento_senha = navegador.find_element(By.NAME, 'password')
            elemento_senha.send_keys("minha_senha")
            elemento_senha.submit()
            logging.info("Tentativa de login enviada.")
            print("Tentativa de login enviada.")
        except Exception as e:
            logging.error(f"Erro ao interagir com a página: {e}")
            print(f"Erro ao interagir com a página: {e}")

    except Exception as e:
        logging.error(f"Erro durante o login: {e}")
        print(f"Erro durante o login: {e}")
    finally:
        navegador.quit()
        logging.info("Navegador encerrado.")
        print("Navegador encerrado.")

if __name__ == "__main__":
    navegador = iniciar_navegador()
    autenticar_instagram(navegador)




