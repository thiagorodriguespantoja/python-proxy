# Usando a imagem base do Python 3.9 slim
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências para o container
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install -r requirements.txt

# Copia o restante dos arquivos do projeto para o container
COPY . .

# Troca o usuário para um usuário de menor privilégio (nobody)
USER nobody

# Comando padrão para iniciar o Celery
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]

