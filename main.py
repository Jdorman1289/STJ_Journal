from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.lang import Builder
from kivy.core.window import Window
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import urllib.request as img_get

Window.size = 640, 640

class MainWindow(MDWidget):

    def jan1(self):
        pass
    
    def jan8(self):
        pass
    
    def jan15(self):
        pass

    def donate(self):
        webbrowser.open_new_tab("")

    def close_two(self):
        exit()

class STJ(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('layouts.kv')


# on launch start main window class
if __name__ == "__main__":
    STJ().run()