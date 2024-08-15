from celery import Celery
from app.auth import login_autenticacao

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def login_autenticacao_task(username, password, user_id):
    login_autenticacao(username, password, user_id)
