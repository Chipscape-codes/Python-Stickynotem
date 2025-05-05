from tkinter import *

root = Tk()
root.title("StickyNoteM")  # title of the window
root.geometry("400x400")  # size of the window
root.configure(bg="black")  # background color of the window


def note():
    box = LabelFrame(root, text="", padx=5, pady=5)
    box.grid(row=0, column=0, padx=5, pady=5)
    text_box = Text(
        box, height=40, width=40, bg="white", fg="black", font=("TimesNewRoman", 12)
    )  # text box
    text_box.pack()
note()

root.mainloop()