from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Listbox, END


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\BALAJI BABA\OneDrive\ドキュメント\figma\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_work():
    task = entry_2.get()
    if task:
        listbox.insert(END, task)
        entry_2.delete(0, END)
    else:
        messagebox.showwarning("To Do App", "Please enter a task.")

def delete_work():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("To Do App", "Please select a task to delete.")

window = Tk()
window.geometry("300x400")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=400,
    width=300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Background image
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
canvas.create_image(
    150.0,
    200.0,
    image=image_image_1
)

# Title text
canvas.create_text(
    71.0,
    16.0,
    anchor="nw",
    text="TO-DO  List",
    fill="#FFFFFF",
    font=("Monoton Regular", 25 * -1)
)

# Input entry background
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
canvas.create_image(
    153.9,
    84.0,
    image=entry_image_2
)

# Input Entry widget
entry_2 = Entry(
    bd=0,
    bg="#D6D5D5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=27.0,
    y=68.0,
    width=253.8,
    height=30.0
)

# Button 1: Add Task
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_work,
    relief="flat"
)
button_1.place(
    x=25.0,
    y=112.0,
    width=121.0,
    height=28.0
)

# Button 2: Delete Task
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=delete_work,
    relief="flat"
)
button_2.place(
    x=158.0,
    y=112.0,
    width=129.0,
    height=28.0
)

# Listbox replacing Text widget for task display
listbox = Listbox(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
listbox.place(
    x=27.0,
    y=161.0,
    width=254.0,
    height=201.0
)

# Footer text
canvas.create_text(
    121.0,
    383.0,
    anchor="nw",
    text="Made by Sowmya",
    fill="#FFFFFF",
    font=("JotiOne Regular", 8 * -1)
)

window.resizable(False, False)
window.mainloop()