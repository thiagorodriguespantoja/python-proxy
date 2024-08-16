import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do proxy
def configurar_proxy(navegador, proxy):
    # Lógica para configurar o proxy no navegador
    pass

def realizar_login(navegador, usuario, senha):
    navegador.get("https://www.instagram.com")
    
    try:
        # Realizando login no Instagram
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(usuario)
        navegador.find_element(By.NAME, "password").send_keys(senha)
        navegador.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

        # Captura de tela após login
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'Instagram')]")))
        screenshot_filename = 'screenshot_after_login.png'
        navegador.save_screenshot(screenshot_filename)
        print(f"Screenshot salvo como {screenshot_filename}")
        
    except Exception as e:
        print(f"Erro durante o login: {str(e)}")

def main():
    proxy = {
        "host": "200.234.133.229",
        "port": "12324",
        "username": "14ad9a9ccd37c",
        "password": "996f9e5a18"
    }
    
    # Inicia o navegador com o proxy configurado
    navegador = uc.Chrome()

    # Configurando proxy no navegador
    configurar_proxy(navegador, proxy)
    
    # Realizando login no Instagram
    realizar_login(navegador, "seu_usuario", "sua_senha")

    # Fechar o navegador
    navegador.quit()

if __name__ == "__main__":
    main()
