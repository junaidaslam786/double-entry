import flet as ft

def main(page: ft.Page):
    # Creating the UI components
    sidebar = ft.Column([ft.Text("Sidebar Content")], width=200)
    app_bar = ft.Row([ft.Text("App Bar")], alignment="center")
    content_area = ft.Column([ft.Text("Content Area")])
    footer = ft.Text("Footer messages")

    # Setting up the main UI layout
    main_area = ft.Column([app_bar, content_area, footer], expand=True)
    ui_layout = ft.Row([sidebar, main_area], expand=True)

    page.add(ui_layout)

if __name__ == "__main__":
    ft.app(target=main)
