
import flet as ft
from core.widgets.header import AppHeader
from core.providers.screen_stack import ScreenManager

def main(page: ft.Page):
    page.title = "AI Agent Chat"
    page.window_width = 1400
    page.window_height = 800
    page.window_left = 400

    screens = ScreenManager()
    header = AppHeader(shrink_handler=screens.home.toggle_shrink)

    page.add(header, screens)

if __name__ == "__main__":
    ft.app(target=main)
