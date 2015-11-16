"""
  This is going to the the image editor provided with the application
"""

__author__ = 'Spencer'

import Tkinter as tk;

# from tk import *;


modes = ["PixelMode", "DoodleMode", "~?VectorMode?~"];
projectmode = 0;
projectdir = "";
projectname = "Untitled";
projectsize = (800, 600);


def startupDialogChoice1Clicked(event):
    global dialog;
    dialog.quit();


def startupDialogChoice2Clicked(event):
    global dialog;
    dialog.quit();


# starts up the project (do you want to open an existing project, or create a new one, etc)
def startup():
    global dialog;
    dialog = tk.Tk();
    message = tk.Label(dialog, "Image Editor");
    choice1 = tk.Button(dialog, text="Open Previous Image");
    choice2 = tk.Button(dialog, text="Create New Image");

    choice1.bind("<Button-Clicked>", startupDialogChoice1Clicked);
    choice2.bind("<Button-Clicked>", startupDialogChoice2Clicked);

    message.grid();
    choice1.grid(row=1);
    choice2.grid(row=2);

    dialog.mainloop();


# setup will actualy set up the data structures to allow for pixel art, ?vector art?, or "doodle" art.
def setup():
    global projectmode;
    if projectmode == 0:
        # we need to set up the data in such a way we keep track of individual pixels.
        pass;
    elif projectmode == 1:
        # we need to set up the data to not care about individual pixels.
        pass;


root = tk.Tk();

drawingCanvas = tk.Canvas(root, width=800, height=600);

root.mainloop();
