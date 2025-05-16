import flet as ft
from typing import Literal

Sender = Literal["bot", "user"]

class ChatBubble(ft.Container):

    def __init__(self, sender: Sender, message_text: str = ""):
        super().__init__()
        self.sender = sender

        self.width = 700  # 1400 // 2
        self.animation = ft.Animation(duration=600, curve=ft.AnimationCurve.DECELERATE)

        icon_name = ft.Icons.COMPUTER if sender == "bot" else ft.Icons.PERSON
        bg_color = ft.Colors.GREY_100 if sender == "bot" else ft.Colors.GREY_300

        self.content = ft.Row(
            controls=[
                ft.Icon(name=icon_name, size=24),
                ft.Markdown(value=message_text, width=self.width),
            ],
            alignment=ft.MainAxisAlignment.START if sender == "bot" else ft.MainAxisAlignment.END
        )

        self.content_chat = ft.Container(
            content=self.content,
            padding=ft.padding.all(10),
            bgcolor=bg_color,
            border_radius=ft.border_radius.all(10),
            margin=ft.margin.only(bottom=10),
        )
