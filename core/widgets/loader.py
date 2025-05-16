import flet as ft
import threading
import time

class LoadingIndicator(ft.Container):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 50
        self.width = 700  # 1400 // 2
        self.bgcolor = ft.Colors.GREY_100
        self.expand = True
        self.border_radius = ft.border_radius.all(10)
        self.padding = ft.padding.all(10)
        self.margin = ft.margin.only(bottom=10)
        self.animation = ft.Animation(duration=600, curve=ft.AnimationCurve.DECELERATE)
        self._scale_state = True

    def _animate_loop(self):
        while True:
            if self._scale_state:
                self.scale = ft.transform.Scale(0.7)
            else:
                self.scale = ft.transform.Scale(1)
            self._scale_state = not self._scale_state
            self.update()
            time.sleep(0.6)

    def start_animation(self):
        thread = threading.Thread(target=self._animate_loop, daemon=True)
        thread.start()
