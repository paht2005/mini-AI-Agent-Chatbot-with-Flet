# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import flet as ft
from ..interface import HomeScreen, NavigationScreen

class ScreenManager(ft.Stack):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True

        self.home = HomeScreen()
        self.navigation = NavigationScreen()

        self.controls = [self.navigation, self.home]
