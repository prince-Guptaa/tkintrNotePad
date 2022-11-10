from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - NotePad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents",
                                                                                      "*.txt")])
    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + "- NotePad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents",
                                                                                                                        "*.txt")])

        if file == "":
            file = None

        else:
          # Save as a New File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + "- NotePad")
        print("File Saved")

    else:
        # Save The File
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("NotePad", "NotePad Created by Prince Gupta")



if __name__ == '__main__':
    root = Tk()
    root.title("Creataing The NotePad.......")
    root.geometry("650x450")
    

    # ADD text Area in notepad

    TextArea = Text(root, font="lucida 13")
    file = None
TextArea.pack(expand=True, fill=BOTH)
# Lets create Menubar

Menubar = Menu(root)
# File Menu Stars in tkinter
FileMenu = Menu(Menubar, tearoff=0)

# To open a new File

FileMenu.add_command(label="New", command=newFile)

# To open alredy exisiting File

FileMenu.add_command(label="Open", command=openFile)

# to current save the file

FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_separator()

FileMenu.add_command(label="Exit", command=quitApp)
Menubar.add_cascade(label="File", menu=FileMenu)

# File Menu Ends in tkinter

# Edit Menu Strats in tkinter

EditMenu = Menu(Menubar, tearoff=0)

# to give a  features Cuts & Copy and Past

EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

Menubar.add_cascade(label="Edit", menu=EditMenu)
# Edit Menu Ends in tkinter

# Help Menu Starts ....

HelpMenu = Menu(Menubar, tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
Menubar.add_cascade(label="Help", menu=HelpMenu)

# Help Menu Ends.....

root.config(menu=Menubar)
# Adding The Scrollbar in the tkiter.....

scroll = Scrollbar(TextArea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)

root.mainloop()
