# Configurações do Celery
broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/0'

# Outras configurações recomendadas para produção
task_serializer = 'json'
accept_content = ['json']
result_serializer = 'json'
timezone = 'UTC'
enable_utc = True
broker_connection_retry_on_startup = True

