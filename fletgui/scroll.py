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
	for category in categories:
		cl.controls.append(
			ft.Text(f"{category[0]} {category[2]} {category[4]}")
		)

	page.add(ft.Container(cl, border=ft.border.all(1)))

ft.app(target=main, assets_dir="assets")