from kivy.lang import Builder
from kivymd.app import MDApp


class appApp(MDApp):

    def build(self):
        self.title = 'KivyMD File Manager'
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"


appApp().run()