# from kivymd.uix.gridlayout import GridLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.label import MDLabel, MDIcon
# from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.list import ThreeLineListItem, MDList, ThreeLineIconListItem, IconLeftWidget, \
#     ThreeLineAvatarListItem, ImageLeftWidget
# from kivy.uix.scrollview import ScrollView
# from kivy.lang import Builder
# from kivymd.theming import ThemeManager # je fais ça si app = kivy.app.App et pas kivymd.app.MDApp

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from helpers import *
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFlatButton

class DemoApp(MDApp):

    def __init__(self, **kwargs):
        # title
        self.title = "Ma deuxieme appli :D"
        # theme
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.theme_style = 'Dark'
        # other variables

        # Screen manager
        self.sm = ScreenManager()
        # super
        super().__init__(**kwargs)

    def build(self):
        # screens
        screen1 = Screen(name="login")

        # button
        button = MDFlatButton(
            text='fromage',
        )
        screen1.add_widget(button)
        
        # Builder
        self.sm.add_widget(screen1)
        return self.sm


if __name__ == "__main__":
    DemoApp().run()
