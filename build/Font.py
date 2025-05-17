import tkinter as tk
from tkinter import font

root = tk.Tk()
root.withdraw()  

available_fonts = list(font.families())

# Example check
font_to_check = "Monoton"
if font_to_check in available_fonts:
    print(f"{font_to_check} is installed!")
else:
    print(f"{font_to_check} is NOT installed.")