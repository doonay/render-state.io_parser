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
    page.title = "Table Header"
    page.fonts = {
        "SpaceMono": "assets/fonts/SpaceMono-Regular.ttf",
        "WorkSans": "assets/fonts/WorkSans-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Settings")
    page.bgcolor = "#2B2B2B"
    page.update()
    
    #---Table header---
    def category_id_sort(e):
        print('category_id_sort')
    def category_sort(e):
        print('category_sort')
    def count_sort(e):
        print('count_sort')
    def status_sort(e):
        print('status_sort')

    category_id = ft.Text(color="#858584", font_family="SpaceMono", size=16, text_align="CENTER",
        spans=[ft.TextSpan(
            "#",
            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
            on_click=category_id_sort)])
    category = ft.Text(color="#858584", font_family="SpaceMono", size=16, text_align="CENTER",
        spans=[ft.TextSpan(
            "Category",
            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
            on_click=category_sort)])
    count = ft.Text(color="#858584", font_family="SpaceMono", size=16, text_align="CENTER",
        spans=[ft.TextSpan(
            "Count",
            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
            on_click=count_sort)])
    status = ft.Text(color="#858584", font_family="SpaceMono", size=16, text_align="CENTER",
        spans=[ft.TextSpan(
            "Status",
            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
            on_click=status_sort)])

    table_header_row = ft.Row([category_id, category, count, status], alignment=ft.MainAxisAlignment.SPACE_AROUND,)
    table_header = ft.Container(
            content=ft.Container(
                content=ft.Column([table_header_row]),
                width='100%',
                height='10%',
                padding=10,
                border_radius=10,
                bgcolor='#2B2B2B'
            ),
            width='100%',
            height='10%',
            border_radius=10,
            bgcolor='#3B3B3B'
        )

    page.add(table_header)
    #---Table header---

ft.app(target=main, assets_dir="assets")



