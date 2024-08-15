from celery import Celery
from app.selenium_auth import usar_proxy_no_selenium

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def autenticar_com_proxies():
    usar_proxy_no_selenium()
