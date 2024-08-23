import os
from datetime import datetime

from kivy.core.text import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.toast import toast
from kivyauth.google_auth import initialize_google, login_google, logout_google
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.list import OneLineIconListItem, TwoLineIconListItem, ThreeLineIconListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from log_me import navigation_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import requests
import json
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.scrollview import ScrollView
from plyer import filechooser

Window.size = (400, 700)


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class FifthScreen(Screen):
    pass


class SixthScreen(Screen):
    pass


class SeventhScreen(Screen):
    pass


class EighthScreen(Screen):
    pass


class NinthScreen(Screen):
    pass


class TenthScreen(Screen):
    pass


class Eleventh_Screen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(FirstScreen(name='signupscreen'))
sm.add_widget(SecondScreen(name='google'))
sm.add_widget(ThirdScreen(name='dob'))
sm.add_widget(FourthScreen(name='main'))
sm.add_widget(FifthScreen(name='screen_login'))
sm.add_widget(SixthScreen(name='page3'))
sm.add_widget(SeventhScreen(name='booking'))
sm.add_widget(EighthScreen(name='screen_app'))
sm.add_widget(NinthScreen(name='scroll'))
sm.add_widget(TenthScreen(name='ten'))
sm.add_widget(Eleventh_Screen(name='success_screen'))


class LokiApp(MDApp):

    #def __init__(self, **kwargs):
     #   super().__init__(**kwargs)
      #  self.ids = None
       # self.task_text = None
        #self.username_text = None
        #self.strng = None
        #self.dob = None
        #self.ids.date_text.text=datetime.now().strftime("%A %d %B %Y")

    def build(self):

        client_id = open("client_id.txt")
        client_secret = open("client_secret.txt")
        initialize_google(self.after_login, self.error_listener, client_id.read(), client_secret.read())

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Red"
        self.help_str = Builder.load_string(navigation_helper)
        self.url = "https://app-data-68264-default-rtdb.firebaseio.com/.json"
        self.url = "https://app-data-68264-default-rtdb.firebaseio.com/.json"
        return self.help_str

    def load_img(self):
        self.url = json.loads(requests.get("https://dog.ceo/api/breeds/image/random").content)['message']
        self.help_str.get_screen('dob').ids.imgg.source = self.url

    # adding task
    def add_task(self):
        self.task_text = self.help_str.get_screen('scroll').ids.task.text
        self.task_da = self.help_str.get_screen('scroll').ids.task_date.text
        self.task_time = self.help_str.get_screen('scroll').ids.time.text
        self.task_phone = self.help_str.get_screen('ten').ids.pho.text
        self.task_breed = self.help_str.get_screen('ten').ids.breed.text
        if self.task_text.split() != []:
            self.help_str.get_screen("page3").ids.task_item.add_widget(
                ThreeLineIconListItem(text=self.task_text, secondary_text=self.task_da, tertiary_text=self.task_time))
            self.help_str.get_screen("page3").ids.task_item.add_widget(
                TwoLineIconListItem(text=self.task_phone, secondary_text=self.task_breed))
            self.help_str.get_screen("page3").manager.current = "page3"

        else:
            Snackbar(text="Please Enter Details ").open()

    def delete_item(self,task_text):
        self.parent.remove_widget(task_text)

    #def select_file(self):
     #   filechooser.open_file(on_selection=self.selected)

    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=['.png', '.jpg', '.jpeg']  # File extensions to filter
        )

    def file_manager_open1(self):
        self.file_manager.show('/')  # Specify the root directory
        self.manager_open = True


#file starts
    def file_manager_open(self):
        filechooser.open_file(on_selection=self.select_path)
    def select_path(self, path):
        try:
            self.root.ids.image.source = path[0]
            self.exit_manager()
            
        except:
            print("fail")

    def exit_manager(self, *args):
        '''
        Called when the user exits the file manager.
        '''
        self.manager_open = False
        self.file_manager.close()


#file ends

    def select_file(self):
        file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        file_manager.show('/')  # You can set the initial directory

    """def select_path(self, path):
        self.exit_manager()
        self.root.ids.container.clear_widgets()

        # Display selected photos and videos
        scroll_view = ScrollView()
        image_list = MDBoxLayout(orientation='vertical', adaptive_height=True, padding=10, spacing=10)
        scroll_view.add_widget(image_list)
        self.root.ids.container.add_widget(scroll_view)

        for file_name in os.listdir(path):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4')):
                if file_name.lower().endswith('.mp4'):
                    # Display video
                    video_label = Label(text=file_name, halign='center')
                    image_list.add_widget(video_label)
                else:
                    # Display image
                    image_tile = SmartTileWithLabel(
                        source=os.path.join(path, file_name),
                        text=file_name,
                        halign='center'
                    )
                    image_list.add_widget(image_tile)


    def whatsupmsg(self):
        import pywhatkit
        pywhatkit.sendwhatmsg("+919902113575", "Happy birthday ", 12, 00)

    def exit_manager(self, *args):
        self.root.ids.container.clear_widgets()
        self.file_manager.close()"""

    #file choose end

    def selected(self, selection):
        #return Image(source=selection[0])
        #if selection:
        try:
            self.ids.image.source = selection[0]
            print(selection[0])
        except:
            pass

    # anther method of login
    def signup(self):
        signupEmail = self.help_str.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.help_str.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.help_str.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])

            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            # to store in firebase
            signup_info = str(
                {f'\"{signupEmail}\":{{"password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.help_str.get_screen('google').manager.current = 'google'

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def phone_number(self):
        PhoneNumber = self.help_str.get_screen('google').ids.name.text
        Name = self.help_str.get_screen('google').ids.phone.text
        # from here to store in firebase
        phone_info = str({f'\"{PhoneNumber}\":{{"phonenumber":\"{Name}\"}}'})
        phone_info = phone_info.replace(".", "-")
        phone_info = phone_info.replace("\'", "")
        to_database = json.loads(phone_info)
        print((to_database))
        requests.patch(url=self.url, json=to_database)
        self.help_str.get_screen('screen_app').manager.current = 'screen_app'

    def address(self):
        Date = self.help_str.get_screen('scroll').ids.task_date.text
        Time = self.help_str.get_screen('scroll').ids.time.text
        Address = self.help_str.get_screen('scroll').ids.task.text
        address_info = str({f'\"{Date}\":{{"time":\"{Time}\","address":\"{Address}\"}}'})
        address_info = address_info.replace(".", "-")
        address_info = address_info.replace("\'", "")
        to_database = json.loads(address_info)
        print((to_database))
        requests.patch(url=self.url, json=to_database)
        self.help_str.get_screen('ten').manager.current = 'ten'

    # google login function
    def after_login(self, name, email, photo_uri):
        self.root.ids.label.text = f"Logged in as {name}"
        self.root.transition.direction = "left"
        self.root.current = "login"

    def error_listener(self):
        print("Login Failed !")

    def login(self):
        login_google()

    def logout(self):
        logout_google(self.after_logout())

    def after_logout(self):
        self.root.ids.label.text = ""
        self.root.transition.direction = "right"
        self.root.current = "main"

    # theme function for app
    def blackwhite(self):

        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Gray"
        else:
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Orange"

    def nav_drawer(self):
        pass

    # date pick
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)#, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date=value.strftime("%A %d %B %Y")
        #self.ids.date_picker.text=str(date)
        print(value)
        print(instance, value, date_range)

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)

    def get_time(self, instance, time):
        self.root.ids.my_time.text = str(time)

    def schedule(self, *args):
        pass

    def on_cancel(self, instance, value):
        print(value)

    def get_date(self, date):
        self.dob = date
        self.strng.get_screen('dob').ids.date_picker.text = str(self.dob)
        self.strng.get_screen('dob').ids.app_screens.disabled = str(self.dob)

    def callback(self, *args):
        toast(args[0])

    def bottom_layer(self):
        data = {
            'Review': "star",
            "chat": "chat",
            "Refer and Earn": "share-all",
            "About Us": "teamviewer",
            "Phone": "phone",
            "Location": "map-marker-plus"
        }
        bottom_sheet = MDGridBottomSheet()
        for item in data.items():
            bottom_sheet.add_item(
                item[0],
                lambda x, y=item[0]: self.callback(y),
                icon_src=item[1]
            )
        bottom_sheet.open()


LokiApp().run()

# RGB colours is 23/255.0,11/255.0,11/255.0,1
