from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import webbrowser

Window.size = 480, 640

persistent_notes = {}

class MainWindow(Screen):

    def display_journal(self, which_day, scripture_reference):
        self.ids.journal_guide.text = f"""
Date: {which_day}

Scripture Reading Plan
   
   Passage: {scripture_reference}

   What is passage about?

   How can I apply it to my life? 

  This Week's Scripture Memory Verse:"


Prayer List

1.
2.
3.
4.
5.
6.


How will you DEVELOP strength today?  

    ____ Bible reading
    ____ Prayer
    ____ Scripture Memory
    ____ Devotional 
    ____ Ministering 
    ____ Fellowship
    ____ Exercise
    ____ Proper diet
    ____ Attitude of fruit of Spirit: joy, peace, 
         hope, faith, love, patience, meekness


 Evening:


 Where did you see God working today? 


Tasks accomplished? 


How did you DEVELOP strength today?  

    Bible reading
    Prayer
    Scripture Memory
    Devotional 
    Ministering 
    Fellowship
    Exercise
    Proper diet
    Attitude of fruit of Spirit:  joy, peace, hope, 
    faith, love, patience, meekness


Where did you display strength today? 

   Spiritual
   Physically
    Mental
   Emotional


One thing you are thankful for tonight:


        """



    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")


class WindowManager(ScreenManager):
    pass

class STJ(MDApp):


    # def edit_saved_item(self, title, body):
    #     screen_manager = self.root
    #     notes_window = screen_manager.get_screen("notes_window")
    #     notes_window.ids.note_text.text = body
    #     self.dialog.content_cls.ids.note_title.text = title.text
        

    # def add_to_list(self, note_title):
    #     screen_manager = self.root
    #     notes_window = screen_manager.get_screen("notes_window")
    #     list_of_notes = notes_window.ids.list_of_notes
    #     note_text = notes_window.ids.note_text.text

    #     persistent_notes[note_title.text] = note_text

    #     for key, value in persistent_notes.items():
   


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layouts.kv')


if __name__ == "__main__":
    STJ().run()