import tkinter as tk
from tkinter import ttk
from ...src.logger import logger

class EncryptionOptions(ttk.LabelFrame):
    
    def __init__(self, master):
        super().__init__(master)
        self["text"] = "Encryption Options"
        self["labelanchor"] = "n"
        
        self.encryption_mode_lb = tk.Label(self, text="Encryption Mode")
        self.encryption_mode_lb.grid(row=0, column=0, pady=5, padx=10)
        
        self.encryption_modes = ("Caesar", "Binary")
        self.current_mode_sv = tk.StringVar(self)
        self.mode_selector_om = ttk.OptionMenu(
            self,
            self.current_mode_sv,
            self.encryption_modes[0],
            *self.encryption_modes,
            command=self.mode_changed)
        self.mode_selector_om.grid(row=0, column=1, pady=5, sticky="w")
        self.mode_spec_widgets = []
        self.mode_changed()
        
        
    def show_caesar_spec(self):
         
        self.key_lb = tk.Label(self, text="Key")
        self.key_lb.grid(row=2, column=0, pady=10)
        self.mode_spec_widgets.append(self.key_lb)
        self.key_intv = tk.IntVar(self)
        self.key_sb = ttk.Spinbox(self, from_=-26, to=26, textvariable=self.key_intv, wrap=True)
        self.key_sb.grid(row=2, column=1)
        self.mode_spec_widgets.append(self.key_sb)
        
    def mode_changed(self, *args):
        
        for widget in self.mode_spec_widgets:
            widget.destroy()
        
        if self.current_mode_sv.get() == "Caesar":
            logger.logging(__name__, 4, "Encryption mode switched to 'Caesar Encryption'")
            self.show_caesar_spec()
            
        elif self.current_mode_sv.get() == "Binary":
            logger.logging(__name__, 4, "Encryption mode switched to 'Binary Encryption'")
            self.show_caesar_spec() 