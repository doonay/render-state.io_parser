import requests
from loguru import logger
from tqdm import trange
from SQLite3.create_table import db_init
from SQLite3.insert_data import insert_one_category

logger.add('cat_parser.log', format="{message}", level="INFO", rotation="5 MB")

db_init()
result = 0
for i in trange(270):
	url = f'https://render-state.to/wp-json/wp/v2/categories/{i}'
	r = requests.get(url)
	if r.status_code == 200:
		data = r.json()
		category = (data['id'], data['name'], data['link'], data['count'])
		result += insert_one_category(category)
logger.info(f'Добавлено {result} категорий')