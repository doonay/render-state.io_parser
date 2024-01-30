import flet as ft

def main(page: ft.Page):
	page.window_width = 600
	page.window_height = 800
	page.window_resizable = True
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.title = "Card"
	page.fonts = {
		"SpaceMono": "assets/fonts/SpaceMono-Regular.ttf",
		"WorkSans": "assets/fonts/WorkSans-Regular.ttf"
	}
	page.theme = ft.Theme(font_family="WorkSans")
	page.update()

	#---HEADER---	
	header_number_text = ft.Text(value = "#")
	header_number_container = ft.Container(
		content=header_number_text,
		alignment=ft.alignment.center,
		bgcolor="#2B2B2B",
		width=50,
		height=50,
		padding=0,
		margin=0,
		expand=False # не растягивать
	)
	header_name_text = ft.Text(value = "Category")
	header_name_container = ft.Container(
		content=header_name_text,
		alignment=ft.alignment.center,
		bgcolor="#2B2B2B",
		width=320,
		height=50,
		expand=True # растягивать
	)
	header_count_text = ft.Text(value = "Count")
	header_count_container = ft.Container(
		content=header_count_text,
		alignment=ft.alignment.center,
		bgcolor="#2B2B2B",
		width=100,
		height=50,
		expand=False # не растягивать
	)
	header_status_text = ft.Text(value = "Status")
	header_status_container = ft.Container(
		content=header_status_text,
		alignment=ft.alignment.center,
		bgcolor="#2B2B2B",
		width=110,
		height=50,
		expand=False # не растягивать
	)
	header_row = ft.Row(
		[header_number_container,header_name_container,header_count_container,header_status_container,],
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
	)
	header_main_inner_container = ft.Container(
		content=header_row,
		margin=2,
		bgcolor="#2B2B2B",
		border_radius=5,
	)
	header_main_outer_container = ft.Container(
		content=header_main_inner_container,
		bgcolor="#3B3B3B",
		border_radius=5,
	)
	page.add(header_main_outer_container)
	#---END HEADER---

	#---TEMP CATEGORY DATA---
	#(id, item_id, category_name, link, count, status)
	category = (256, 2, 'Genesis 8 Female',	'https://render-state.to/cat/daz-studio/', 50240, 1)
	#---END TEMP CATEGORY DATA---

	#---CARD LISTENER---
	def update_status(status_value: bool):
		#print('Формируем апдэйт запрос:')
		#print('таблица: categories')
		#print('где айди =', 'ХЗ')
		#print('апдейтим поле status на значение:', status_value)
		pass
	def sort_by_id(e):
		pass
	def sort_by_category_name(e):
		pass
	def sort_by_count(e):
		pass
	def sort_by_status(e):
		pass
	def switch_label_changed(e):
		if switcher.value:
			status_label.color = "GREEN"
			status_label.value = "tracked"
			switcher.value = True
		else:
			status_label.color = "RED"
			status_label.value = "ignored"
			switcher.value = False
		page.update()
		#update_status(switcher.value)
	#---END CARD LISTENER---

	
	#---CARD ---
	#id from db
	item_number = ft.Text( 
		value=category[0],
		color="WHITE",
		font_family="SpaceMono"
		)
	item_number_with_circle = ft.Container(content=item_number,border_radius=25,width=30,height=30,bgcolor="#2B2B2B",alignment=ft.alignment.center)
	item_number_container = ft.Container(content=item_number_with_circle,alignment=ft.alignment.center,bgcolor="#3B3B3B",width=50,height=50,
	expand=False # не растягивать
	)

	category_name_text = ft.Text(
		spans=[
			ft.TextSpan(
				category[2],
				url=category[3],
			),
		], size=26
	)
	category_container = ft.Container( 
			content=category_name_text,
			alignment=ft.alignment.center,
			bgcolor="#3B3B3B",
			width=320,
			height=50,
			expand=True # растягивать
		)
	count_text = ft.Text(category[4])
	count_container = ft.Container(
			content=count_text,
			alignment=ft.alignment.center,
			bgcolor="#3B3B3B",
			width=100,
			height=50,
			expand=False # не растягивать
		)
	switcher = ft.Text("SWITCHER")
	status_label = ft.Text(
		color = "GREEN",
		value="tracked",
		font_family="RobotoSlab")

	status_label_container = ft.Container(
		content=status_label,
		alignment=ft.alignment.center,
		bgcolor="#3B3B3B",
		width=50,
		height=50,
		expand=False # не растягивать
	)
	switcher = ft.Switch(
		active_color="WHITE",
		value=bool(category[5]),
		on_change=switch_label_changed)
	switcher_container = ft.Container(
			content=switcher,
			alignment=ft.alignment.center,
			bgcolor="#3B3B3B",
			width=60,
			height=50,
			expand=False # не растягивать
		)

	card_row = ft.Row([
		item_number_container,
		category_container,
		count_container,
		status_label_container,
		switcher_container,
	],
	alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
	page.add(card_row)
	#---END ITEM CARD---

ft.app(target=main, assets_dir="assets")



