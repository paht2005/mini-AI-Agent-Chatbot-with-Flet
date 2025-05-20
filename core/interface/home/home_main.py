# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import flet as ft
from core.animations import AnimationHelper
from core.widgets import ChatBubble, LoadingIndicator
from core.model_llm import query_answer

class HomeScreen(ft.Container):

    def __init__(self):
        super().__init__()
        self.width = 1400
        self.expand = True
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.all(10)

        self.chat_list = ft.ListView(
            width=self.width,
            height=600,
            controls=[
                ChatBubble("bot", message_text="Hi! How can I assist you today?"),
                ChatBubble("user", message_text="I have a problem with my account."),
            ]
        )

        self.input_field = ft.TextField(
            hint_text="Enter message...",
            expand=True,
        )

        self.input_area = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.INSERT_EMOTICON, size=24),
                    self.input_field,
                    ft.IconButton(
                        icon=ft.Icons.SEND,
                        icon_size=24,
                        on_click=self.process_message
                    ),
                ]
            )
        )

        self.content = ft.Column(
            controls=[self.chat_list, self.input_area]
        )

    def toggle_shrink(self, e: ft.ControlEvent):
        AnimationHelper.toggle_shrink(self, e)

    def process_message(self, e: ft.ControlEvent):
        user_text = self.input_field.value.strip()
        if not user_text:
            return

        loading = LoadingIndicator()
        self.chat_list.controls.append(ChatBubble("user", message_text=user_text))
        self.chat_list.controls.append(loading)
        self.chat_list.update()

        # Gọi agent trả lời
        response = query_answer(user_text)

        self.chat_list.controls.remove(loading)
        self.chat_list.controls.append(ChatBubble("bot", message_text=response))
        self.chat_list.update()
        self.input_field.value = ""
        self.input_field.update()

