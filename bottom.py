
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.core.window import Window

Window.size = (300, 530)
"""
<IntroScreen>
    name: "intro_screen"

    MDBoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: intro_screen_toolbar
            title: '[font=Gabriola][size=40][color=#FD0101]First[/color][/size][size=28]project[/size][/font]'
            right_action_items: [["calendar-month", lambda x: app.change_screen('to_do_screen')]] #links to to-do listss screen

        MDCard:
            orientation: 'vertical'
            padding: 16
            size_hint: None, None
            size: "280dp", "360dp"
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - intro_screen_toolbar.height - dp(90)
            y: root.height - intro_screen_toolbar.height - dp(50)
            elevation: "8dp"
            orientation: 'vertical'
            radius: 15

            ScrollView:
                MDLabel:
                    markup: True
                    size_hint_y: None
                    size: self.texture_size
                    text:
                        

        MDBottomAppBar:
        MDToolbar:
        icon: 'book-lock-open' #links to 'ways'
        on_action_button: app.change_screen('ways_screen')
        type: "bottom"
        mode: "center"
        elevation: "8dp"
        left_action_items: [["home", lambda x: x], ["account-group", lambda x: app.change_screen("success_screen")]]
        right_action_items: [["magnify", lambda x: app.change_screen("search_screen")], ["menu", lambda x: app.change_screen("menu_screen")]]


<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"

<SuccessScreen>
    name: "success_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: success_screen_toolbar
            title: "Success Stories"
            right_action_items: [["progress-clock", lambda x: app.change_screen('goals_screen')]]

        ScrollView:
            MDGridLayout:
                cols: 1
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)

                MyTile:
                    source: "C:/Users/HP USER/Downloads/bella_baron.jpg"
                    text: "[size=26]Cat 1[/size]\\n[size=14]cat-1.jpg[/size]"

                    on_release:
                        app.root.current = 'bella_baron'

                MyTile:
                    source: "C:/Users/HP USER/Downloads/bella_baron.jpg"
                    text: "[size=26]Cat 2[/size]\\n[size=14]cat-2.jpg[/size]"
                    tile_text_color: app.theme_cls.accent_color

                MyTile:
                    source: "C:/Users/HP USER/Downloads/bella_baron.jpg"
                    text: "[size=26][color=#ffffff]Cat 3[/color][/size]\\n[size=14]cat-3.jpg[/size]"
                    tile_text_color: app.theme_cls.accent_color

        MDBottomAppBar:
            MDToolbar:
                icon: 'magnify'
                on_action_button: app.change_screen('search_screen')
                type: "bottom"
                mode: "center"
                elevation: "8dp"
                left_action_items: [["home", lambda x: app.change_screen("intro_screen")], ["account-group", lambda x: x]]
                right_action_items: [["magnify", lambda x: app.change_screen("search_screen")], ["menu", lambda x: app.change_screen("menu_screen")]]


 <SearchScreen>
     name: "search_screen"

    FloatLayout:
         MDBottomAppBar:
            MDToolbar:
                icon: 'window-close'
                type: "bottom"
                mode: "center"
                elevation: "8dp"
                left_action_items: [["home", lambda x: app.change_screen("intro_screen")], ["account-group", lambda x: app.change_screen("success_screen")]]
                right_action_items: [["magnify", lambda x: x], ["menu", lambda x: app.change_screen("menu_screen")]]

        MDTextField:
            mode: 'fill'
            hint_text: "Search"
            pos_hint: {"center_x": .5,"center_y": .9}
            size_hint_x: None
            width: 280

<MenuScreen>
    name: "menu_screen"

    BoxLayout:
        orientation: "vertical"
        md_bg_color: (240/255, 240/255, 240/255, 1)

        MDToolbar:
            id: menu_screen_toolbar
            title: "Tools"
            elevation: "8dp"

        MDCard:
            orientation: 'vertical'
            padding: 16
            size_hint: None, None
            size: "280dp", "360dp"
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - menu_screen_toolbar.height - dp(90)
            y: root.height - menu_screen_toolbar.height - dp(50)
            elevation: 8
            orientation: 'vertical'
            radius: 15

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "Calendar"
                        on_release:
                            app.root.current = "calendar_screen"
                        IconLeftWidget:
                            icon: "calendar-month"
                    OneLineIconListItem:
                        text: "Extra"
                        on_release:
                            app.root.current = "extra_screen" 
                        IconLeftWidget:
                            icon: "notebook-multiple"
                    OneLineIconListItem:
                        text: "Archive"
                        on_release:
                            app.root.current = "archive_screen"
                        IconLeftWidget:
                            icon: "archive"
                    OneLineIconListItem:
                        text: "contact Us"
                        on_release:
                            app.root.current = "contact_info_screen"
                        IconLeftWidget:
                            icon: "email-mark-as-unread"


        MDBottomAppBar:
            MDToolbar:
                icon: 'reload'
                type: "bottom"
                mode: "center"
                elevation: "8dp"
                left_action_items: [["home", lambda x: app.change_screen("intro_screen")], ["account-group", lambda x: app.change_screen("success_screen")]]
                right_action_items: [["magnify", lambda x: app.change_screen("search_screen")], ["menu", lambda x: x]]


<WaysScreen>
    name: "ways_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: ways_screen_toolbar
            title: "How-tos"
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('intro_screen')]]
            elevation: "8dp"

        ScrollView:

            MDGridLayout:
                cols: 1
                adaptive_height: True
                spacing: 10
                padding: 10

                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    Image:
                        source: "C:/Users/HP USER/Downloads/bella_baron.jpg"

                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello dear'

                    ScrollView:
                        MDLabel:
                            size_hint_y: None
                            size: self.texture_size
                            text:
                                Hello, World
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello boss'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello goodness'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello hi'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello yes?'

<To_DoScreen>
    name: "to_do_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: to_do_screen_toolbar
            title: 'To-Do-List'
            right_action_items: [['plus', lambda x: x]]
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('intro_screen')]]

        MDCard:
            orientation: 'vertical'
            padding: 16
            elevation: 8
            radius: 15
            size_hint: None, None
            size: '280', '360'
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - to_do_screen_toolbar.height + dp(10)
            y: root.height - to_do_screen_toolbar.height - dp(20)


<GoalsScreen>
    name: 'goals_screen'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: goals_screen_toolbar
            title: 'Goals'
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('success_screen')]]

        MDCard:
            orientation: 'vertical'
            padding: 16
            size_hint: None, None
            size: "280dp", "360dp"
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - goals_screen_toolbar.height + dp(10)
            y: root.height - goals_screen_toolbar.height - dp(20)
            elevation: "8dp"
            orientation: 'vertical'
            radius: 15

<BellaBaron>
    name: 'bella_baron'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: bella_baron_toolbar
            title: "Bella Baron"
            left_action_items: [["keyboard-backspace", lambda x: app.change_screen('success_screen')]]
            right_action_items: [["progress-check", lambda x: app.change_screen('goals_screen')]]

        ScrollView:

            MDGridLayout:
                cols: 1
                adaptive_height: True
                spacing: 10
                padding: 10

                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    Image:
                        source: "C:/Users/HP USER/Downloads/bella_baron.jpg"

                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello dear'

                    ScrollView:
                        MDLabel:
                            size_hint_y: None
                            size: self.texture_size
                            text:
                                
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello boss'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello goodness'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello hi'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello yes?'


<CalendarScreen>
    name: "calendar_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: calendar_screen_toolbar
            title: 'Calendar'
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('menu_screen')]]
            right_action_items: [['calendar', lambda x: x]] # on press returns today's date

        MDCard:
            orientation: 'vertical'
            padding: 16
            elevation: 8
            radius: 15
            size_hint: None, None
            size: '280', '360'
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - calendar_screen_toolbar.height + dp(10)
            y: root.height - calendar_screen_toolbar.height - dp(20)

<ExtraScreen>
    name: "extra_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: extra_screen_toolbar
            title: 'Extra'
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('menu_screen')]]

        ScrollView:

            MDGridLayout:
                cols: 1
                adaptive_height: True
                spacing: 10
                padding: 10

                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    Image:
                        source: "C:/Users/HP USER/Downloads/bella_baron.jpg"

                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello dear'

                    ScrollView:
                        MDLabel:
                            size_hint_y: None
                            size: self.texture_size
                            text:
                            
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello boss'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello goodness'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello hi'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "130dp"
                    radius: 15
                    caption: 'Hello yes?'

<ArchiveScreen>
    name: "archive_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: archive_screen_toolbar
            title: 'Archive'
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('menu_screen')]]

        MDCard:
            orientation: 'vertical'
            padding: 16
            elevation: 8
            radius: 15
            size_hint: None, None
            size: '280', '360'
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - archive_screen_toolbar.height + dp(10)
            y: root.height - archive_screen_toolbar.height - dp(20)

<Contact_InfoScreen>
    name: "contact_info_screen"

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: contact_info_screen_toolbar
            title: 'Contact Info'
            left_action_items: [['keyboard-backspace', lambda x: app.change_screen('menu_screen')]]

        MDCard:
            orientation: 'vertical'
            padding: 16
            elevation: 8
            radius: 15
            size_hint: None, None
            size: '280', '360'
            pos_hint: {"center_x": .5, "center_y": .6}
            height: root.height - contact_info_screen_toolbar.height + dp(10)
            y: root.height - contact_info_screen_toolbar.height - dp(20)

            ScrollView:
                MDLabel:
                    size_hint_y: None
                    size: self.texture_size
                    text:
                        """


class IntroScreen(Screen):
    pass


class WaysScreen(Screen):
    pass


class To_DoScreen(Screen):
    pass


class SuccessScreen(Screen):
    pass


class GoalsScreen(Screen):
    pass


class BellaBaron(Screen):
    pass


class SearchScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class CalendarScreen(Screen):
    pass


class ExtraScreen(Screen):
    pass


class ArchiveScreen(Screen):
    pass


class Contact_InfoScreen(Screen):
    pass


class TenThousandApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '200'
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(IntroScreen(name="intro_screen"))
        self.sm.add_widget(WaysScreen(name="ways_screen"))
        self.sm.add_widget(To_DoScreen(name="to_do_screen"))
        self.sm.add_widget(SuccessScreen(name="success_screen"))
        self.sm.add_widget(GoalsScreen(name="goals_screen"))
        self.sm.add_widget(BellaBaron(name="bella_baron"))
        self.sm.add_widget(SearchScreen(name="search_screen"))
        self.sm.add_widget(MenuScreen(name="menu_screen"))
        self.sm.add_widget(CalendarScreen(name="calendar_screen"))
        self.sm.add_widget(ExtraScreen(name="extra_screen"))
        self.sm.add_widget(ArchiveScreen(name="archive_screen"))
        self.sm.add_widget(Contact_InfoScreen(name="contact_info_screen"))

        return self.sm

    def change_screen(self, screen):
        self.sm.current = screen


TenThousandApp().run()
