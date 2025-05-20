# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import flet as ft
from typing import Callable, Optional

class AppHeader(ft.Container):
    def __init__(self, shrink_handler: Optional[Callable[[ft.ControlEvent], None]] = None):
        super().__init__()

        self.height = 50
        self.width = 1400
        self.bgcolor = ft.Colors.DEEP_PURPLE_500
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.only(right=10)

        menu_button = ft.IconButton(
            icon=ft.Icons.MENU,
            icon_size=24,
            icon_color=ft.Colors.WHITE,
            on_click=shrink_handler
        )
        avatar_icon = ft.CircleAvatar(
            content=ft.Icon(ft.Icons.PERSON, size=24, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.PURPLE_500
        )

        self.content = ft.Row(
            controls=[menu_button, avatar_icon],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
