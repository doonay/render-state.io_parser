import flet as ft
import sqlite3
'''
page.window_width = 600
page.window_height = 800
page.window_resizable = True
page.vertical_alignment = ft.MainAxisAlignment.CENTER
page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
page.fonts = {
	"Settings": "assets/fonts/SpaceMono-Regular.ttf",
	"CategoryName": "assets/fonts/WorkSans-Regular.ttf"
}
page.theme = ft.Theme(font_family="Settings")
page.update()
'''

def main(page: ft.Page):
	page.title = "Scroll"

	connection = sqlite3.connect('render-state.db')
	cur = connection.cursor()
	cur.execute("SELECT * FROM categories")
	categories = cur.fetchall()

	w, h = 600, 800
	page.window_width = w
	page.window_height = h
	page.window_resizable = False

	cl = ft.Column(
		spacing=10,
		height=h-60,
		width=w,
		scroll=ft.ScrollMode.ALWAYS,
		on_scroll_interval=0,
		
	)
	'''
	def switch_label_changed(e):
		status_label.value = ("tracked" if switcher.value else "ignored")
		status_label.color = ("GREEN" if switcher.value else "RED")
		print('апдэйт запрос в таблицу с категориями, поле status значение:', switcher.value)
		page.update()
	'''
	def get_bool_value(db_value: int):
		if db_value == 1:
			return True
		else:
			return False


	 #---CARD---
	def switch_label_changed(e):
		print('---')
		status_label.value = ("tracked" if switcher.value else "ignored")
		status_label.color = ("GREEN" if switcher.value else "RED")
		print('Формируем апдэйт запрос:')
		print('таблица: categories')
		print('где айди =', 'ХЗ')
		print('апдейтим поле status на значение:', switcher.value)
		page.update()
	#---END CARD---

	def some():
		print(some)

	for category in categories:
		#---CARD---

		cat = ft.Text(f"{category}")
		
		#category_id = ft.Text(f"{category[0]}", key=str(category[0]))
		category_id = ft.Text(value=category[0], color="#858584", font_family="SpaceMono", size=16, text_align="CENTER",)
		circle_category_id_container = ft.Container(content=category_id, bgcolor="WHITE", border_radius=0, width=35, height=25, alignment=ft.alignment.center,)

		#name = ft.Text(f"{category[2]}", key=str(category[0]))
		name = ft.Text(spans=[
				ft.TextSpan(
					category[2],
					url=category[3],
				),
			], size=26
		)

		#count = ft.Text(f"{category[4]}", key=str(category[0]))
		count = ft.Text(value=category[4], size=26,)

		status = ft.Text(f"{category[5]}")
		status_label = ft.Text(color = "GREEN", value="tracked", size=26, font_family="RobotoSlab")
		switcher = ft.Switch(active_color="WHITE", value=True, on_change=switch_label_changed)

		'''
		card_row = ft.Row([circle_container, category, count, status_label, switcher], alignment=ft.MainAxisAlignment.SPACE_AROUND,)
		'''
		card_row = ft.Row([circle_category_id_container, name, count, switcher], alignment=ft.MainAxisAlignment.SPACE_AROUND,)
		card = ft.Container(content=ft.Column([card_row]), width='80%', padding=10, bgcolor="BLACK")
		#---END CARD---
		cl.controls.append(card)

	
	page.add(
		ft.Container(cl, border=ft.border.all(1)),
	)

ft.app(target=main, assets_dir="assets")