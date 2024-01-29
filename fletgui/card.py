import flet as ft

def main(page: ft.Page):
    def switch_label_changed(e):
        print(switcher.value)
        status_label.value = ("tracked" if switcher.value else "ignored")
        status_label.color = ("GREEN" if switcher.value else "RED")
        page.update()

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
    page.theme = ft.Theme(font_family="Settings")
    page.update()
    
    #---Card---
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

    '''
    ПРОПИСАТЬ В КАРТОЧКУ ССЫЛКУ ДЛЯ ПЕРЕХОДА НА САЙТ ПОСМОТРЕТЬ ДЕТАЛИ!
    xxx = ft.Text(spans=[
            ft.TextSpan("AwesomeApp 1.0 "),
            ft.TextSpan(
                "Visit our website",
                ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                url="https://google.com",
                on_enter=status_sort,
                on_exit=status_sort,
            ),
        ],
    )
    page.add(xxx)
    '''
    #---EndCard---

    page.add(card)

ft.app(target=main, assets_dir="assets")



