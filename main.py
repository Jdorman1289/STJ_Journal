from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import webbrowser

Window.size = 640, 640


saved_list = []

class MainWindow(Screen):

    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")


class NotesWindow(Screen):

    def add_note(self):
        #to be added
        pass


class NavBar(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class STJ(MDApp):

    def set_screen(self, screen_name):
        self.root.current = screen_name

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('layouts.kv')

# on launch start main window class
if __name__ == "__main__":
    STJ().run()