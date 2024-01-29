import flet as ft

def main(page: ft.Page):
    #---switcher listener---
    def switch_label_changed(e):
        print(switcher.value)
        status_label.value = ("tracked" if switcher.value else "ignored")
        status_label.color = ("GREEN" if switcher.value else "RED")
        page.update()

    #---APP SETTINGS---
    page.window_width = 600
    page.window_height = 800
    page.window_resizable = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Flet example"
    page.fonts = {
        "Settings": "assets/fonts/SpaceMono-Regular.ttf",
        "CategoryName": "assets/fonts/WorkSans-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Settings")
    #---END APP SETTINGS---

    #---HEADER---
    title_label = ft.Text(color = "WHITE",value="Settings",size=30,font_family="Settings",weight=ft.FontWeight.W_100,)
    close_icon = ft.Image(src="assets/icons/close.png")
    row = ft.Row([title_label, close_icon],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(row)
    #---END HEADER---
    page.add(ft.Divider())
    #---CARD---
    category_id = ft.Text(value=1, color="#858584", font_family="SpaceMono", size=16, text_align="CENTER",)
    circle_container = ft.Container(content=category_id, bgcolor="WHITE", border_radius=50, width=25, height=25, alignment=ft.alignment.center,)
    category = ft.Text(value="Genesis 8 Female", size=26,)
    count = ft.Text(value="45689", size=26,)
    status_label = ft.Text(color = "GREEN", value="tracked", size=26, font_family="RobotoSlab")
    switcher = ft.Switch(active_color="WHITE", value=True, on_change=switch_label_changed)
    card_row = ft.Row([circle_container, category, count, status_label, switcher], alignment=ft.MainAxisAlignment.SPACE_AROUND,)
    card = ft.Card(
        content=ft.Container(
            content=ft.Column([card_row]), width='80%', padding=10,)
    )
    page.add(card)
    #---END CARD---

ft.app(target=main, assets_dir="assets")



