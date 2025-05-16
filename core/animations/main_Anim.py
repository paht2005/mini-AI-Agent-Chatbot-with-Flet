
import flet as ft

class AnimationHelper:

    @staticmethod
    def toggle_shrink(control: ft.Control, event: ft.ControlEvent):
        if not hasattr(control, "_is_shrunk"):
            control._is_shrunk = False
        
        if control._is_shrunk:
            control._is_shrunk = False
            control.scale = ft.transform.Scale(1, alignment=ft.alignment.center_right)
        else:
            control._is_shrunk = True
            control.scale = ft.transform.Scale(0.65, alignment=ft.alignment.center_right)
        
        control.update()

