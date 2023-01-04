from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
import webbrowser

Window.size = 640, 640


saved_list = []

class MainWindow(MDWidget):

    def jan1(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=004b4A")
            
    def jan8(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpB")
    
    def jan15(self):
        webbrowser.open_new_tab("https://www.blueletterbible.org/tools/MultiVerse.cfm?s=008QpD")

    def save_entry(self):
        # Get the input fields and card
        title_input = self.ids['title_input']
        body_input = self.ids['body_input']
        entry_card = self.ids['entry_card']

        # Get the values from the input fields
        title = title_input.text
        body = body_input.text
        
        new_card = MDCard()
        box_layout = MDBoxLayout(orientation='vertical')

        entry_card.add_widget(new_card)
        new_card.add_widget(box_layout)

        # Add the title and body as labels to the box layout
        box_layout.add_widget(MDLabel(text=title, font_style='H6'))   
        box_layout.add_widget(MDLabel(text=body))

        # Set the elevation of the card
        new_card.elevation = 2

        # Clear the input fields
        title_input.text = ''
        body_input.text = ''

class STJ(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('layouts.kv')

# on launch start main window class
if __name__ == "__main__":
    STJ().run()