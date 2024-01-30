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
	
	header_number_text = ft.Text(
		value = "Clickable with Ink"
		)
	header_number_container = ft.Container(
		content=header_number_text,
		margin=10,
		padding=10,
		alignment=ft.alignment.center,
		bgcolor=ft.colors.BLACK,
		width=150,
		height=150,
		border_radius=10,
		ink=True,
		on_click=lambda e: print("Clickable with Ink clicked!"),
	)
	header_row = ft.Row(
		[header_number_container,],
		alignment=ft.MainAxisAlignment.CENTER,
	)
	page.add(header_row)

	#-----------------------ниже карточки, выше заголовок

	item_number = ft.Text( #циферка из базы !!!done!!!
		value="100",
		color="BLACK",
		font_family="SpaceMono"
		)
	item_number_with_circle = ft.Container( #кружок под циферкой !!!done!!!
			content=item_number,
			border_radius=25,
			width=30,
			height=30,
			bgcolor="WHITE",
			alignment=ft.alignment.center
		)
	item_number_container = ft.Container( #контейнер под циферку из базы
		#animate#bgcolor#blend_mode#blur#border#border_radius#clip_behavior#gradient#image_fit#image_opacity#image_repeat#image_src#image_src_base64#ink#shadow#shape#theme_mode#theme#url#url_target
		#---События#on_click#on_hover#on_long_press
		content=item_number_with_circle,
		alignment=ft.alignment.center,
		bgcolor=ft.colors.AMBER,
		width=50,
		height=50,
		#border_radius=50,
		padding=0,
		margin=0,
		expand=False # не растягивать
	)
	category_name_text = ft.Text("Daz Studio")
	category_container = ft.Container( # name from db
			content=category_name_text,
			#margin=10,
			#padding=10,
			alignment=ft.alignment.center,
			bgcolor=ft.colors.RED,
			width=320,
			height=50,
			#border_radius=10,
			#border=ft.border.all(2, ft.colors.RED),
			expand=True # растягивать
		)
	count_text = ft.Text("50240")
	count_container = ft.Container(
			content=count_text,
			#margin=10,
			#padding=10,
			alignment=ft.alignment.center,
			bgcolor=ft.colors.GREEN,
			width=100,
			height=50,
			#border_radius=10,
		)
	switcher = ft.Text("SWITCHER")
	switcher_container = ft.Container(
			content=switcher,
			#margin=10,
			#padding=10,
			alignment=ft.alignment.center,
			bgcolor=ft.colors.RED,
			width=100,
			height=50,
			#border_radius=10,

		)
	card_row = ft.Row([
		item_number_container,
		category_container,
		count_container,
		switcher_container,

	],
	alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
	)

	page.add(
		ft.Container(
			content=card_row,
			#margin=10,
			#padding=10,
			#alignment=ft.alignment.center,
			bgcolor=ft.colors.BLACK,
			#width='100%',
			#height=80,
			#border_radius=10,
		)
	)

	# avatar with failing foreground image and fallback text
	circle_number = ft.CircleAvatar(
		foreground_image_url="https://avatars.githubusercontent.com/u/_5041459?s=88&v=4",
		content=ft.Text("100"),
	)
	page.add(circle_number)

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
	def some():
		print(some)

	#---END CARD---


	#category = (id, item_id, category_name, link, count, status)
	category = (1, 2, 'Daz Studio',	'https://render-state.to/cat/daz-studio/', 50240, 1)
	#cat = ft.Text(f"{category}")

	#---CARD---

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

	page.add(card)

ft.app(target=main, assets_dir="assets")



