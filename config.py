import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv('REDIS_URL')
PROXY_LIST_PATH = os.getenv('PROXY_LIST', 'proxies.json')
