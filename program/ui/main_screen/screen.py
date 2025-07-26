import tkinter as tk
from . import input_output_fr, encryption_options_fr

class MainScreen(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.encryption_options_fr = encryption_options_fr.EncryptionOptions(master)
        self.encryption_options_fr.grid(row=0, column=0, sticky="ew", pady=50, padx=20)
        
        self.input_output_fr = input_output_fr.InputOutput(master)
        self.input_output_fr.grid(row=1, column=0, padx=20, pady=20)            