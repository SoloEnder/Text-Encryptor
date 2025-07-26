import tkinter as tk
from .main_screen.screen import MainScreen

class Window(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Text Encryptor")
        self.main_screen_fr = MainScreen(self)
        self.main_screen_fr.grid()