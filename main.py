from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import json
import webbrowser

Window.size = 480, 640

try:
    file = open('notes.json', 'r')
    persistent_notes = json.load(file)
except:
    persistent_notes = {}

day_selected = ""

class MainWindow(Screen):

#     def create_about(self):
#         self.ids.about_text.text = """

# VISION:

# We are a Great Commission Church with every member on mission with God.
 
# MISSION:

# First Baptist Church of Brownsville is a multi-cultural, multi-linguistic ministry bringing Jesus Christ to Brownsville, the Rio Grande Valley, Mexico, and the world, through our worship, discipleship, and love.

# PURPOSE:

# First Baptist Church exists to exalt the Savior in worship, equip the saints through Biblical discipleship, extend Christ’s salvation by witnessing and church planting, and express the love of Jesus to all people by our service and compassion.
# Exalt the Savior
# Equip the Believer
# Extend the Gospel to all Peoples
# Express Christ's Love

# VALUES:

# At First Baptist Church of Brownsville we value people because Jesus values people.
# Everything we do will be in fulfillment of our purposes.
# Everything we do will be done with excellence.
# Everything we do will be done because of love and in a loving manner.
# Everything we do will help us to better reach people with the Gospel of Jesus Christ.
    
# """

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

    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")


class WindowManager(ScreenManager):
    pass

class STJ(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('layouts.kv')
    

if __name__ == "__main__":
    STJ().run()