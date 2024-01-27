from tkinter import *

# Список кольорів і назв функцій
colors = [
    ("Red", "#fc0303", "red"),
    ("Orange", "#fc8003", "orange"),
    ("Yellow", "#fcfc03", "yellow"),
    ("Green", "#07fc03", "green"),
    ("Blue", "#03fcf0", "blue"),
    ("Deep blue", "#0a02e0", "deepBlue"),
    ("Pink", "#e84adb", "pink"),
    ("Purple", "#7a0070", "purple"),
    ("Gray", "#696268", "gray"),
    ("Black", "#0a0a0a", "black")
]

def set_color(color_name, color_code, entry_left, entry_right):
    entry_left.delete(0, END)
    entry_left.insert(0, color_name)
    entry_right.delete(0, END)
    entry_right.insert(0, color_code)

root = Tk()
root.title('Layout Example')
root.geometry('600x500')

for color_name, color_code, command_name in colors:
    frame = Frame(root)
    frame.pack()

    entry_left = Entry(frame, justify='center', bd=2)
    entry_left.pack(side='left', padx=10, pady=10)

    entry_right = Entry(frame, justify='center', bd=2)
    entry_right.pack(side='right', padx=10, pady=10)

    button = Button(frame, width=40, bg=color_code, fg='white', command=lambda name=color_name, code=color_code, left=entry_left, right=entry_right: set_color(name, code, left, right))
    button.pack(padx=10, pady=10)

root.mainloop()