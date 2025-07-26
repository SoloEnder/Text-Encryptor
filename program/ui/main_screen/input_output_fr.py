import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class InputOutput(ttk.LabelFrame):
    
    def __init__(self, master):
        super().__init__(master)
        self["text"] = "Input/Ouput"
        self["labelanchor"] = "n"
        
        self.input_lb = tk.Label(self, text="Input", font=("default 9"))
        self.input_lb.grid(row=0, column=0, sticky="w", pady=20)
        
        self.input_st = ScrolledText(self, width="30", height="10", font=("helvetica 8"))
        self.input_st.grid(row=1, column=0, padx=20, pady=10)
        
        self.input_lb = tk.Label(self, text="Output", font=("default 9"))
        self.input_lb.grid(row=0, column=2, sticky="e")
        
        self.output_st = ScrolledText(self, width="30", height="10", font=("helvetica 8"), state="disabled")
        self.output_st.grid(row=1, column=2, padx=20, pady=10)
        
        self.reverse_icon = tk.PhotoImage(file="program/assets/reverse_icon.png")
        self.reverse_b = ttk.Button(self, image=self.reverse_icon)
        self.reverse_b.image = self.reverse_icon
        self.reverse_b.grid(row=1, column=1)
        
        self.translate_b = ttk.Button(self, text="Encrypt")
        self.translate_b.grid(row=1, column=1, sticky="s", pady=10)