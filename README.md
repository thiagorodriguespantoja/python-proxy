# Python Proxy Automation with Selenium and Celery

## Descrição do Projeto

Este projeto foi criado para automatizar o processo de autenticação no Instagram utilizando proxies brasileiros em um ambiente Python. O sistema permite realizar autenticações automatizadas em modo headless com Selenium, garantindo que o IP seja localizado no Brasil, independentemente da localização do servidor onde o código está sendo executado. O uso de proxies é essencial para evitar bloqueios de login ao acessar contas do Instagram hospedadas em servidores fora do país de origem.

O projeto utiliza Docker Compose para gerenciar facilmente os containers, e Celery para o agendamento de tarefas assíncronas que executam o processo de autenticação. Esse setup permite a rotação de proxies em intervalos de tempo especificados, proporcionando uma maior segurança e flexibilidade na automação.

## Tecnologias Utilizadas

- **Python 3.12**
- **Selenium** (Modo headless para automação de browser)
- **Celery** (Tarefas assíncronas)
- **Docker e Docker Compose** (Orquestração de containers)
- **Redis** (Broker de mensagens para o Celery)
- **Proxies HTTP/SOCKS5** (Localizados no Brasil)

## Estrutura do Projeto

```plaintext
/python-proxy
│
├── /app
│   ├── __init__.py               # Indica que 'app' é um pacote Python
│   ├── auth.py                   # Contém a função de autenticação 'login_autenticacao'
│   ├── selenium_auth.py          # Configura o Selenium com proxies e executa a automação de login
│   ├── tasks.py                  # Integração das tarefas do Celery com a automação Selenium
│   ├── utils.py                  # Funções utilitárias, como o carregamento de proxies
│   ├── main.py                   # Arquivo principal para iniciar o Celery ou executar a autenticação manualmente
│   ├── proxies.json              # Arquivo que contém os dados dos proxies
│
├── /tests
│   ├── __init__.py               # Indica que 'tests' é um pacote Python
│   └── test_auth.py              # Contém o teste da função 'login_autenticacao'
│
├── /logs                         # Diretório para armazenamento de logs
│   └── selenium_logs.log         # Arquivo de log para monitorar eventos do Selenium
│
├── /output                       # Diretório para armazenar capturas de tela tiradas pelo Selenium
│   └── screenshot_instagram.png  # Screenshot após o login no Instagram
│
├── .env                          # Variáveis de ambiente (não incluído no repositório)
├── config.py                     # Arquivo de configuração do projeto
├── docker-compose.yml            # Configuração do Docker Compose
├── Dockerfile                    # Dockerfile para construir a imagem da aplicação
├── README.md                     # Este arquivo
├── requirements.txt              # Dependências Python
└── tasks.py                      # Tarefas Celery
```

## Setup do Ambiente

### Pré-requisitos

- **Docker** e **Docker Compose** instalados
- **Python 3.12+** instalado localmente (caso queira rodar o projeto localmente sem Docker)

### 1. Clonar o Repositório

```bash
git clone https://github.com/thiagorodriguespantoja/python-proxy.git
cd python-proxy
```

### 2. Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o conteúdo abaixo (adapte conforme necessário):

```env
REDIS_URL=redis://localhost:6379/0
PROXY_LIST=app/proxies.json
```

### 3. Configurar o Docker e Dependências

**1. Instalar dependências (localmente ou no container Docker)**:
- Localmente (opcional):
  ```bash
  pip install -r requirements.txt
  ```

**2. Configurar o Docker Compose**:
- Build e execução dos containers:
  ```bash
  docker-compose up --build
  ```

Isso irá configurar e rodar o Selenium em modo headless e o Redis para o Celery.

### 4. Executar o Celery e o Processo de Autenticação

O arquivo `main.py` permite executar tanto o Celery quanto o processo de autenticação manual com proxies.

- **Iniciar o Celery Worker**:
  ```bash
  python app/main.py celery
  ```

- **Executar o Processo de Autenticação Manualmente**:
  ```bash
  python app/main.py auth
  ```

### 5. Testar o Projeto

Você pode rodar os testes usando `pytest` para garantir que tudo está funcionando corretamente:

```bash
pytest
```

Os testes estão localizados no diretório `tests/` e cobrem a funcionalidade de autenticação.

### 6. Configurar Proxies

Os proxies usados para a rotação devem ser definidos em um arquivo `proxies.json` no formato:

```json
[
    {
        "host": "proxy1.example.com",
        "port": "1080",
        "username": "user1",
        "password": "pass1"
    },
    {
        "host": "proxy2.example.com",
        "port": "1080",
        "username": "user2",
        "password": "pass2"
    }
]
```

### 7. Rotação de Proxies

O projeto está configurado para rodar automaticamente a rotação de proxies em intervalos definidos, o que é essencial para evitar que o Instagram bloqueie acessos de locais suspeitos.

### 8. Logs e Capturas de Tela

Logs detalhados são gerados durante o processo de autenticação e são armazenados na pasta `/logs`. Além disso, capturas de tela são feitas automaticamente e armazenadas na pasta `/screenshots` para ajudar na depuração.

## Contribuições

Sinta-se à vontade para fazer fork deste repositório, abrir pull requests ou relatar problemas. Contribuições são sempre bem-vindas!

---

### Finalidade do Projeto

O objetivo principal deste projeto é fornecer uma maneira automatizada de autenticar no Instagram utilizando proxies brasileiros, mesmo quando hospedado em servidores fora do Brasil. Isso é crucial para evitar problemas de bloqueio de login devido à discrepância de localização geográfica. Com o uso do Celery para agendamento de tarefas e a rotação de proxies, o sistema se mantém robusto e eficiente para operações prolongadas.

