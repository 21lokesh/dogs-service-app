from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from plyer import filechooser

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Image Upload"
        left_action_items: [["menu", lambda x: app.file_manager_open()]]

    FloatLayout:

        Image:
            id: image
            source: ''

        MDRoundFlatButton:
            text: "Upload Image"
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: app.file_manager_open()
'''

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def file_manager_open(self):
        filechooser.open_file(on_selection=self.select_path)

    def select_path(self, path):
        try:
            self.root.ids.image.source = path[0]
            self.exit_manager()
        except:
            print("failed")

    def exit_manager(self, *args):
        self.file_manager.close()

MyApp().run()