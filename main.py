from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

Window.size = (350, 580)


class SegScreen(MDScreen):
    pass


class Checkboxes(MDScreen):
    pass


class MainApp(MDApp):
    values = []

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("tela.kv"))
        screen_manager.add_widget(Builder.load_file("segunda.kv"))
        return screen_manager

    def fechar(self):
        self.stop()

    def on_start(self):
        checkbox = Checkboxes
        return checkbox

    def check1(self, checkbox, active):
        if active:
            print("10")

    def check2(self, checkbox, active):
        if active:
            print("0")
<<<<<<< HEAD


=======
>>>>>>> 925a06f53f20dcbfd82a7bee0fd893a931b74981


if __name__ == "__main__":
    LabelBase.register(name="MPoppins",
                       fn_regular="C:\\Users\\ARTHUR GAMER4\\PycharmProjects\\aplicativocomercial\\Poppins\\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins",
                       fn_regular="C:\\Users\ARTHUR GAMER4\\PycharmProjects\\aplicativocomercial\\Poppins\\Poppins-SemiBold.ttf")

MainApp().run()
