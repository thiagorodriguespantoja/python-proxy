from celery import Celery
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Celery('tasks', broker='redis://redis:6379/0')

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

