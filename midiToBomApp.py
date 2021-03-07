import tkinter

from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.messagebox import showinfo

import midiToBom
import os


class Menubar(ttk.Frame):
    """Builds a menu bar for the top of the main window"""
    def __init__(self, parent, *args, **kwargs):
        ''' Constructor'''
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_menubar()

    def on_exit(self):
        '''Exits program'''
        quit()

    def display_about(self):
        '''Displays help document'''
        #self.new_win = tkinter.Toplevel(self.root) # Set parent
        os.system("start " + "about.txt")
        pass


    def init_menubar(self):
        self.menubar = tkinter.Menu(self.root)
        self.menu_file = tkinter.Menu(self.menubar) # Creates a "File" menu
        self.menu_file.add_command(label='Exit', command=self.on_exit) # Adds an option to the menu
        self.menubar.add_cascade(menu=self.menu_file, label='File') # Adds File menu to the bar. Can also be used to create submenus.

        self.menu_help = tkinter.Menu(self.menubar)
        self.menu_help.add_command(label='Open About .txt', command=self.display_about)
        self.menubar.add_cascade(menu=self.menu_help, label='About')

        self.root.config(menu=self.menubar)



def popup_bonus():
    win =ttk.Toplevel()
    win.wm_title("Window")

    l =ttk.Label(win, text="Input")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def popup_showinfo():
    showinfo("Done", "All done! BPM to Timing Points")
    
    
def file_loaded(fileName):
    showinfo("File was loaded", fileName)
        

def browseFiles():
    workingdir = Path.cwd()
    filename = filedialog.askopenfilename(initialdir = workingdir,
                                          title = "Select a File",
                                          filetypes = (("Midi files","*.mid*"),("Reaper files","*.rpp*")))
    
#   file_loaded(filename)
    return str(filename)

def browseFileBom():
    workingdir = Path.cwd()
    filename = filedialog.askopenfilename(initialdir = workingdir,
                                          title = "Select a File",
                                          filetypes = (("Bom files","*.bom*"),("Bom files","*.bom*")))
    
#   file_loaded(filename)
    return str(filename)

def convertToBom(fileName, fileNameBom):
    print(fileName)
    if ".mid" in fileName:
        midiToBom.RunFromFiles_MIDI(fileName,fileNameBom)
        popup_showinfo()

    elif ".rpp" in fileName:
        midiToBom.RunFromFiles_RPP(fileName,fileNameBom)
        popup_showinfo()
       
       
class GUI(ttk.Frame):
    """Main GUI class"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.fileName = ""
        self.fileNameBom = ""
        self.init_gui()


    def openwindow(self):
        #self.new_win = tkinter.Toplevel(self.root) # Set parent
        #SomethingWindow(self.new_win)
        self.fileName = browseFiles()
        if self.fileNameBom != "":
            self.btn2["state"] = "normal"
        
    def openwindow2(self):
        self.fileNameBom = browseFileBom()
        if self.fileName != "":
            self.btn2["state"] = "normal"
    
    
    def convert(self):
        self.btn2["state"] = "disable"
        convertToBom(self.fileName, self.fileNameBom)


    def init_gui(self):
        self.root.title("MIDI to BOM Converter")
        self.root.wm_iconbitmap('bbicon.ico')

        windowSize = "416x512"
        
        self.root.geometry(windowSize)
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1) # Allows column to stretch upon resizing
        self.grid_rowconfigure(0, weight=1) # Same with row
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.option_add('*tearOff', 'FALSE') # Disables ability to tear menu bar into own window
             
        path = Path.cwd()
        load = Image.open(path / "bblogo.jpg").resize((384,384))
        render = ImageTk.PhotoImage(load)
        self.img = ttk.Label(self, image=render)
        self.img.image = render
        self.img.place(x=0, y=0)  
        
        
        # Menu Bar
        self.menubar = Menubar(self.root)
        
        # Create Widgets
        self.btn = ttk.Button(self, text='Browse .mid/.rpp', command=self.openwindow)
        
        
        self.btn1= ttk.Button(self, text='Browse .bom', command= self.openwindow2)


        self.btn2 = ttk.Button(self, text='Convert BPM', command= self.convert)
        
        if self.fileName == "" or self.fileNameBom == "":
            self.btn2["state"] = "disabled"


        # Layout using grid
        self.btn.grid(row=1, column=0, sticky='ew')

        self.btn1.grid(row=2, column=0, sticky='ew')
        
        self.btn2.grid(row=3, column=0, sticky='ew')

        self.img.grid(row=0, column=0, sticky='ew')


        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=5)
            

root = tkinter.Tk()
GUI(root)
root.mainloop()
