import requests
from bs4 import BeautifulSoup
from headers import headers

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
		headers = {
			'authority': 'render-state.to',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control': 'max-age=0',
			'cookie': 'cf_clearance=vXBZsqmvoHWQ09lA6kW3SkMwL_uyjbWIDy6eP1uOs2Y-1706217984-1-ATwikEpJXOGUe9aynLGSn54WZ/D2NWFbjSS+ObwJ+r8SOWWCze4ebP1TiGvLPFaogom8yh1G9y2Xyj1HiqwI4F0=; _iub_cs-35772605=%7B%22timestamp%22%3A%222024-01-25T21%3A33%3A10.918Z%22%2C%22version%22%3A%221.54.0%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%222%22%3Afalse%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%225%22%3Afalse%7D%2C%22id%22%3A%2235772605%22%2C%22cons%22%3A%7B%22rand%22%3A%22601865%22%7D%7D; euconsent-v2=CP48G0AP48G0AB7E8BENAkEgAAAAAAAAAAAAAABBQgIgA4AM-AjwBKoCZwG-AO2AdyBBQCRAElAJRgS0AmOBMkCaQQUABQkFsABAAC4AKAAqABwADwAIIAXgBhADIANQAeABEACYAFUAMwAbwA9AB-AEJAIYAiQBHACWAE0AMAAYcAygDLAGyAOeAdwB3wD2APiAfYB-wD_AQAAikBFwEYAI1ASIBJQCUwE_AUGAqACrgFzAL0AYoA0QBtADcAHEgR6BIoCdgFDgKPAUiAtgBcgC7wF5gMGAYbAyMDJAGTgMzAZzA1cDWQG3gNzAbqA4IByYDlwHjgPpAgmBBgCEMELQQuAhzBD0EPwI4wR9BH8CRQEkIJMAkyBLACWYEtwJfATAAmYBM4CbgE5gJ0gTuCDUOg4AALgAoACoAHAAQQAuADUAHgARAAmABVgC4ALoAYgAzABvAD0AH6AQwBEgCWAE0AJwAUYAwABhgDKAGiANkAc8A7gDvAHtAPsA_QB_wEUARiAjoCSgEpgJ-AoMBUQFXALEAXOAvIC9AGKANoAbgA4gB1AD7AIvgR6BIoCVAEyAJ2AUPAo8CkAFNAKsAWKAsqBbAFsgLdAXAAuQBdoC7wF5gL6AYMAw0Bj0DIwMkAZOAyoBlgDMwGcgNEAaaA1WBq4GsANvAbqA4sByYDlwHjgPJAfSA-sB9wD-wIAgQYAhbBDkEOgIegRxAjtBH0EfwJFASQAkyBKgCWAEswJdAS-AmABMwCZwE3AJvAThAnMBOmCdoJ3EIHAACwAKAAuABiADUAJgAUwAqgBcADEAG8APQAjgBgADngHcAd4A_wCKAEpAKDAVEBVwC5gGKANoAdQBHoCVAFNAKsAWKAsoBaIC4AFyAMjAZOAzkBogDVQHAAPHAfSA_sCDAEKAIWgQ6Ah6BHECRQEkAJMgS6AmcBOYCdxKBuAAgABYAFAAOQAwADEAHgARAAmABVAC4AGKAQwBEgCOAFGAMAAbIA7wB-QFRAVcAuYBigDqAImARfAj0CRQFHgKaAWKAsoBbAC84GRgZIAycBnIDWAG3gOAAfSBAECB4EGAIQgQ9AjiBIoCSAEmQJdAS-AmYBM4CbgE4QJzATuKQVwAFwAUABUADgAIIAYABqADwAIgATAApABVADEAGYAP0AhgCJAFGAMAAZQA0QBsgDnAHfAPwA_QCLAEYgI6AkoBKQCgwFRAVcAuYBeQDFAG0ANwAdQA9oB9gETAIvgR6BIoCdgFDgKQAU0AqwBYoC2AFwALkAXaAvMBfQDDYGRgZIAycBlgDOYGsAayA28BuoDggHJgOXAeKA8cB9ID-wIJgQYAhCBC0CGcEOQQ6AjiBHaCPoI_gSKAkhBJgEmQJZgS6Al8BMACZgEzgJvATmAncAAA; _iub_cs-35772605-granular=%7B%22gac%22%3A%22MX4%3D%22%7D',
			'referer': 'https://render-state.to/p/dt-joana-for-genesis-8-female/',
			'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
		}
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
	url = 'https://render-state.to/cat/genesis-8-1-female/'
	main(url)