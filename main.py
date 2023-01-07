from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
import webbrowser

Window.size = 480, 640

class SettingsList(OneLineIconListItem):
    divider = None
    icon = StringProperty()

class MainWindow(Screen):

    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")


class NotesWindow(Screen):

    def save_note(self):
        #to be added
        pass
    def discard_note(self):
        #to be added
        pass


class NavBar(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class STJ(MDApp):

    def set_screen(self, screen_name):
        self.root.current = screen_name

    dialog = None

    def notes_settings(self):

        if not self.dialog:
            self.dialog = MDDialog(
                title="Settings",
                type="simple",
                items=[
                    SettingsList(text="Save Note",icon="content-save-outline"),
                    SettingsList(text="Discard Draft",icon="delete-alert-outline"),
                ],
            )
        self.dialog.open()


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layouts.kv')


if __name__ == "__main__":
    STJ().run()