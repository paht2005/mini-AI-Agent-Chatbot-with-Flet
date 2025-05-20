# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import flet as ft

class NavigationScreen(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1400
        self.expand = True
        self.bgcolor = ft.Colors.WHITE

        self.content = ft.Column(
            controls=[
                ft.Text("Navigation Screen Placeholder")
            ]
        )
