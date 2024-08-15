from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.utils import carregar_proxies

def configurar_selenium_com_proxy(proxy):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Adiciona o proxy às opções do Selenium
    options.add_argument(f'--proxy-server={proxy}')

    navegador = webdriver.Chrome(options=options)
    return navegador

def usar_proxy_no_selenium():
    proxies = carregar_proxies()
    for proxy in proxies:
        proxy_url = f"socks5://{proxy['username']}:{proxy['password']}@{proxy['host']}:{proxy['port']}"
        
        # Configura o navegador Selenium com o proxy
        navegador = configurar_selenium_com_proxy(proxy_url)
        
        # Exemplo de uso: Acessar o Instagram com o proxy configurado
        try:
            navegador.get("https://www.instagram.com")
            print(f"Autenticando com proxy: {proxy_url}")
            
            # Continue com a lógica de autenticação no Instagram aqui...
            # Por exemplo, inserir credenciais de login
            
        except Exception as e:
            print(f"Erro ao acessar o site com o proxy {proxy_url}: {str(e)}")
        
        finally:
            # Fechar o navegador após o uso
            navegador.quit()