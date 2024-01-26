import requests
from bs4 import BeautifulSoup
from headers import headers

headers = headers

def get_pagination(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	pagination = int(soup.find('div', {'class': 'nav-links'}).find_all('a', {'class': 'page-numbers'})[-2].text)
	return pagination

def get_one_page_data():
	pass
def get_detail_data(url):
	ищем данные тут div class single_post
			
	print(date)
	print(title)
	print(img)
	print(description)
	print(support_link)
	print(mega_link)
	print(mediafire_link)
	print(google_drive_link)


def main(url):
	pagination = get_pagination(url)
	#for i in range(1, pagination+1, 1):
	for i in range(1, 2, 1):
		url = f'https://render-state.to/cat/genesis-8-1-female/page/{i}/'
		print(url)
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'lxml')
		cards = soup.find('div', {'id': 'content_box'}).find_all('article', {'class': 'latestPost excerpt'})
		for card in cards:
			#отсюда качаем маленькую картинку
			# !!!подготовить картинку адулт и не качать её!!! Эта картинка везде одна и та же!
			https://render-state.to/wp-content/uploads/2024/01/parental-70-244x317.jpg
			https://render-state.to/wp-content/uploads/2024/01/parental-67-244x317.jpg
			https://render-state.to/wp-content/uploads/2024/01/parental-65-244x317.jpg
			#ищем ссылку, куда провалиться (она же и уникальный идентификатор записи)
			#проваливаемся
			itemdata = get_detail_data(url)
			#добавляем данные в базу
			result = insert_data(item_data)
			#записываем результат в лог
			
			
if __name__ == '__main__':
	url = 'https://render-state.to/cat/genesis-8-1-female/'
	main(url)