import flet as ft

def main(page: ft.Page):
    def switch_label_changed(e):
        print(switcher.value)
        status_label.value = ("tracked" if switcher.value else "ignored")
        status_label.color = ("GREEN" if switcher.value else "RED")
        page.update()

    page.window_width = 600        # window's width is 200 px
    page.window_height = 800       # window's height is 200 px
    page.window_resizable = True  # window is not resizable
    #page.update()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Flet example"
    page.fonts = {
        "Settings": "assets/fonts/SpaceMono-Regular.ttf",
        "CategoryName": "assets/fonts/WorkSans-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Settings")
    page.update()

    title_label = ft.Text(
        #color = "GREEN",
        value="Settings",
        size=30,
        font_family="Settings",
        weight=ft.FontWeight.W_100,
    )
    row = ft.Row([title_label],alignment=ft.MainAxisAlignment.CENTER)
    page.add(row)

    status_label = ft.Text(
        color = "GREEN",
        value="tracked",
        size=26,
        font_family="RobotoSlab",
        weight=ft.FontWeight.W_100,
    )

    
    switcher = ft.Switch(
        active_color="WHITE",
        #active_track_color="BLUE",
        #adaptive=True,
        #autofocus=True,
        #focus_color="RED",
        #inactive_thumb_color="GREEN",
        #inactive_track_color="BLACK",
        #label="tracked",
        #label_position=ft.LabelPosition.LEFT,
        #thumb_color="YELLOW",
        #thumb_icon="DEFAULT",
        #track_color="DEFAULT",
        value=True,
        on_change=switch_label_changed)#, label_position=ft.LabelPosition.LEFT)
    
    row = ft.Row([status_label, switcher],alignment=ft.MainAxisAlignment.CENTER)
    page.add(row)
    #col = ft.Column(col)
    
    
    page.update()
    '''
    page.add(
        ft.Row(
            controls=[
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C"),
                switcher
            ]
        )
    )
    
    
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
                ft.DataColumn(ft.Text("Last name")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                        ft.DataCell(ft.Text("Smith")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                        ft.DataCell(ft.Text("Smith")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                        ft.DataCell(ft.Text("Smith")),
                    ],
                ),
            ],
        ),
    )
    '''


    

    


ft.app(target=main, assets_dir="assets")



