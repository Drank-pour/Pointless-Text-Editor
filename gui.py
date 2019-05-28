import tkinter as tk
from tkinter import filedialog
from tkinter import *
import msvcrt as ms
class Application(Frame):
    def createWidgets(self):
        root.title('Text Editor')
        self.QUIT =  Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(column = 3, row = 3)

        self.browseLabel = tk.LabelFrame(self,text = "Open A File")
        self.browseLabel.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.fileLabel = tk.Label(self, text="--")
        self.fileLabel.grid(column = 2, row = 2)
        self.saveButton()
        self.browseButton()
        
    def browseButton(self):
        self.button = tk.Button(self.browseLabel, text = "Browse A File", command=self.fileDiaog)
        self.button.grid(column = 1, row = 1)



    def fileDiaog(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetype = (("text", "*.txt"), ("All Files", "*")))
        self.fileLabel.configure(text = self.fileName)
        self.readFile()
        self.delimiter()

    def saveButton(self):
        self.button = tk.Button(self, text = "Save",fg = "green", command=self.saveContent)
        self.button.grid(column = 2, row = 1)

    def readFile(self):
        with open(self.fileName) as f:
            self.displayData(f.read())
    

    def displayData(self, textData):
        self.txtArea = Text(self, height = 40, width = 100, wrap=WORD)
        self.txtArea.insert('1.0',textData)
        self.txtArea.grid(column=2,row=3)

    def delimiter(self):
        self.delimitEntry = Entry()
        self.delimitEntry.grid(column = 4, row = 1)
        self.delimitButton = Button(self, text = "Delmit", command = self.delmit)
        self.delimitButton.grid(column = 4, row = 2)
        
    def delmit(self):
            self.delimitText = self.delimitEntry.get()
            self.splitEntry = self.txtArea.get('1.0', "end-1c")
            self.lines = self.splitEntry.replace(self.delimitText, "\n")
            self.delmitedText = self.txtArea.insert('1.0', self.lines)

    def saveContent(self):
        self.editedText = self.txtArea.get('1.0', "end-1c")
        with open(self.fileName, "w+") as f:
            f.write(self.editedText)

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid(column = 4, row = 4)
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
