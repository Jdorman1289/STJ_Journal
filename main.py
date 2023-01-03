from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
import webbrowser

Window.size = 640, 640


class MainWindow(MDWidget):

    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")

    def add_note(self):
        note_text = self.ids['note_text']
        notes_list = self.ids['notes_list']
            
        notes_list.add_widget(MDLabel(text=note_text.text), index=len(notes_list.children))
        note_text.text = ""

class STJ(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('layouts.kv')

# on launch start main window class
if __name__ == "__main__":
    STJ().run()