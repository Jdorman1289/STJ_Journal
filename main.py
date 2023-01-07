from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
import webbrowser

Window.size = 480, 640

class SettingsList(OneLineIconListItem):
    divider = None
    icon = StringProperty()

class NoteTitle(BoxLayout):
    pass

class MainWindow(Screen):

    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")


class NotesWindow(Screen):
    pass

class NavBar(Screen):
    pass

class WindowManager(ScreenManager):
    pass



class STJ(MDApp):

    dialog = None

    def set_screen(self, screen_name):
        self.root.current = screen_name


    def save_note(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Note Title",
                type="custom",
                content_cls=NoteTitle(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )           
        self.dialog.open()

        # note_text = self.ids.note_text.text
        # list_of_notes = self.ids.list_of_notes
        # note_title = self.ids.note_title.text


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layouts.kv')


if __name__ == "__main__":
    STJ().run()