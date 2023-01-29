from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import webbrowser

__version__ = "1.0.0"

try:
    file = open('notes.json', 'r')
    persistent_notes = json.load(file)
except:
    persistent_notes = {}

day_selected = ""

class MainWindow(Screen):


    def about(self):
        webbrowser.open_new_tab("https://www.fbcbrownsville.com/who-we-are/")

    def display_journal(self, which_day, scripture_reference):

        self.day_selected = which_day
        for key, value in persistent_notes.items():
            if key == which_day:
                self.ids.journal_questions_text.text = value
 


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

    def save_note(self):

        try:
            persistent_notes[self.day_selected] = self.ids.journal_questions_text.text

            json_notes = json.dumps(persistent_notes)
            f = open("notes.json","w")
            f.write(json_notes)
            f.close
        except:
            pass


    def open_passage(self, book, chapter):
        webbrowser.open_new_tab(f"https://www.blueletterbible.org/nasb20/{book}/{chapter}/1/s_936001")


class WindowManager(ScreenManager):
    pass

class STJ(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layouts.kv')
    

if __name__ == "__main__":
    STJ().run()