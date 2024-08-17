from celery import Celery
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do Celery
app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

# Carrega as configurações do arquivo celeryconfig.py (se existir)
app.config_from_object('celeryconfig')

@app.task
def acessar_instagram():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Configura o Selenium para se conectar ao Selenium Server
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )

    # Exemplo de navegação
    driver.get('https://www.instagram.com')
    print(f"Título da página: {driver.title}")

    driver.quit()

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    # Testa a tarefa adicionando 4 e 6
    result = add.delay(4, 6)
    print(f"Resultado da soma: {result.get(timeout=10)}")



