__author__ = 'Spencer'

from Tkinter import *;
from ScrolledText import ScrolledText;
"""
    this is a not permanent scripting window so that for now, we can type our lwsl and run it, contained in a ui
"""

def run(event):
    global scriptInput;
    #run
    code = scriptInput.get("1.0", "end-1c");
    print(code);

root = Tk();

rootFrame = Frame(root, width=800, height=600);
rootFrame.pack();

scriptInput = ScrolledText(rootFrame);
scriptButton = Button(rootFrame, text="Run");
scriptButton.bind("<ButtonPress>", run);

scriptInput.grid(columnspan=2);
scriptButton.grid(row=5, column=1, sticky=E);

root.mainloop();