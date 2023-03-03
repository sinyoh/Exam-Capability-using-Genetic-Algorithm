from tkinter import *
from tkinter.ttk import *

from root import *
from home import Home
from settings import Settings

def disp_home():
    home.show_home()
    settings.hide_settings()

def disp_settings():
    settings.show_settings()
    home.hide_home()

# ! MENU
home = Home()
settings = Settings()

menubar = Menu(root)
# file = Menu(menubar, tearoff = 0)
menubar.add_command(label='Home', command=disp_home)
# menubar.add_command(label='Output', command=None)
menubar.add_command(label='Settings', command=disp_settings)
# menubar.add_command(label='Help', command=None)

# menubar.add_cascade(label='File', menu = file)

# file.add_command(label='Home', command=disp_home)
# file.add_command(label='Settings', command=disp_settings)
# file.add_command(label='Output', command = None)
# file.add_separator()
# file.add_command(label='Exit', command = root.destroy)


root.configure(menu=menubar)
root.mainloop()