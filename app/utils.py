import json
import os

# Função para carregar proxies do arquivo JSON
def carregar_proxies(proxies_file="app/proxies.json"):
    with open(proxies_file, 'r') as file:
        proxies = json.load(file)
    return proxies
