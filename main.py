from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
import webbrowser

Window.size = 480, 640

persistent_notes = {}

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

class WindowManager(ScreenManager):
    pass

class STJ(MDApp):

    dialog = None

    def set_screen(self, screen_name):
        self.root.current = screen_name

    def edit_saved_item(self, title, body):
        screen_manager = self.root
        notes_window = screen_manager.get_screen("notes_window")
        notes_window.ids.note_text.text = body
        self.dialog.content_cls.ids.note_title.text = title.text
        
    # def remove_list_item(self):

    def new_note(self):
        screen_manager = self.root
        notes_window = screen_manager.get_screen("notes_window")
        notes_window.ids.note_text.text = ""
        self.dialog.content_cls.ids.note_title.text = ""


    def add_to_list(self, note_title):
        screen_manager = self.root
        notes_window = screen_manager.get_screen("notes_window")
        list_of_notes = notes_window.ids.list_of_notes
        note_text = notes_window.ids.note_text.text

        persistent_notes[note_title.text] = note_text
        list_of_notes.clear_widgets()

        for key, value in persistent_notes.items():
            list_of_notes.add_widget(
                TwoLineListItem(
                    text=key,
                    secondary_text=value,
                    on_press = lambda key=key, value=value: self.edit_saved_item(key,value),
                    on_release = lambda x: notes_window.ids.nav_drawer.set_state("closed")
                )
            )


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
                        on_press=lambda x: self.add_to_list(self.dialog.content_cls.ids.note_title),
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                ],
            )           
        self.dialog.open()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layouts.kv')


if __name__ == "__main__":
    STJ().run()