import requests
from bs4 import BeautifulSoup
from headers import headers
from SQLite3.select_data import select_all_categories, select_category_by_id, select_category_by_item_id, select_category_by_category_name
import sys

headers = headers

def get_pagination(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	pagination = int(soup.find('div', {'class': 'nav-links'}).find_all('a', {'class': 'page-numbers'})[-2].text)
	return pagination

def get_one_page_data():
	pass

def get_detail_data(url):
	print(url)
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	item = soup.find('div', {'id': 'content_box'}).div#.find('div', {'class': 'single_post'})
	item_id = item.get('id')
	print(item_id)

	print(card)
	header = card#.header

	
	'''			
	print(date)
	print(title)
	print(img)
	print(description)
	print(support_link)
	print(mega_link)
	print(mediafire_link)
	print(google_drive_link)
	'''
	return header

def main(url):
	pagination = get_pagination(url)
	for i in range(1, pagination+1, 1):
		url = f'https://render-state.to/cat/genesis-8-1-female/page/{i}/'
		print(url)
		r = requests.get(url, headers=headers)
		print(r.xml())
		'''
		soup = BeautifulSoup(r.text, 'lxml')
		cards = soup.find('div', {'id': 'content_box'}).find_all('article', {'class': 'latestPost excerpt'})
		for card in cards:
			#отсюда качаем маленькую картинку
			# !!!подготовить картинку адулт и не качать её!!! Эта картинка везде НЕ одна и та же!
			# так же завести поле с пометкой адулт или нет
			#https://render-state.to/wp-content/uploads/2024/01/parental-70-244x317.jpg
			#https://render-state.to/wp-content/uploads/2024/01/parental-67-244x317.jpg
			#https://render-state.to/wp-content/uploads/2024/01/parental-65-244x317.jpg
			#ищем ссылку, куда провалиться (она же и уникальный идентификатор записи)
			#проваливаемся
			
			#ищем данные тут div class single_post
			url = card.a.get('href')
			itemdata = get_detail_data(url)
			#print(itemdata)
			sys.exit()
			break
		break
			#добавляем данные в базу
			#result = insert_data(item_data)
			#записываем результат в лог
		'''
			
if __name__ == '__main__':
	categories = select_all_categories()
	for cat in categories:
		print(cat['category_name'])
	
	#print(type(categories))
	#
	#print(type(cat))
	'''
	print(cat.id)
	print(cat.item_id)
	print(cat.category_name)
	print(cat.count)
	'''

	'''
	#print("Query all tasks:")
	#print(select_all_categories())
	#print("Query category by category_name like Genesis 9:")
	#print(select_category_by_category_name('Genesis 9'))
	#print("Query category by id = 5:")
	#print(select_category_by_id(5))
	#print("Query category by item_id = 156:")
	#print(select_category_by_item_id(156))
	#print("Query category by category_name like Necromancer 8.1:")
	#print(select_category_by_category_name('Necromancer 8.1'))
    

	если разбивать таблицу, то запрос на селект потом джойнить
	Select * from card t1 join author t2 on t1.fk_id = t2.id where t2.author_name = …
	
	url = 'https://render-state.to/cat/genesis-8-1-female/'
	main(url)
	'''
