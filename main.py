from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

Window.size = (350, 580)


class MDExtendedFabButton:
    pass


class SegScreen(MDScreen, MDExtendedFabButton):
    pass



class MainApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("tela.kv"))
        screen_manager.add_widget(Builder.load_file("segunda.kv"))



        return screen_manager

    def fechar(self):
        self.stop()

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="C:\\Users\\ARTHUR GAMER4\\PycharmProjects\\aplicativocomercial\\Poppins\\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="C:\\Users\ARTHUR GAMER4\\PycharmProjects\\aplicativocomercial\\Poppins\\Poppins-SemiBold.ttf")

MainApp().run()