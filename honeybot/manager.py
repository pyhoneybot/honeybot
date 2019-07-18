from tkinter import *
import tkinter as tk
import os
import inspect
import configparser

#Create a window with a title
window = tk.Tk()
window.geometry("650x670")
window.title("Manager")
	
#Gets the system path for the manager file
filePath = os.path.abspath(inspect.getfile(inspect.currentframe()))
extenstion = filePath[-11]
#gets the system path for the plugin folder
pluginPath = filePath[0:filePath.index("manager.py")] + "plugins"
#Switches to the config file dir
configPath = filePath[0:filePath.index("manager.py")] + "settings" + extenstion + "PLUGINS.conf"

def saveFile():
	s = tt.get(1.0,END)
	f = open(configPath, 'wt')
	f.write(s)
	f.close()

def getPlugins(dirName):
	listOfFile = os.listdir(dirName)
	return listOfFile	

def clicked():
	selected = [listbox.get(pos) for pos in listbox.curselection()]
	for file in selected:
		tt.insert(END, file + "\n")

pluginList = getPlugins(pluginPath);

MainLabel = Label(window, text="Select the plugins you wish to load and add them to the config file")
MainLabel.grid(row=0, column=0)

saveBtn = Button(window, text="Save File", width=10, command=saveFile)
saveBtn.grid(row=6, column=0)

addBtn = Button(window, text="Add Plugin", width=10, command=clicked)
addBtn.grid(row=2, column=0)

label2 = Label(window, text="Editable PLUGINS.conf :")
label2.grid(row=3,column=0)

label3 = Label(window, text="Don't forget to hit save!")
label3.grid(row=5,column=0)

tt = Text(window, width= 80)
tt.grid(row=4,column=0)
tt.insert(END, open(configPath).read())

listbox = Listbox(window, width=60)
listbox.grid(row=1, column=0)
for name in pluginList:
	if(name[-2:] == "py"):
		listbox.insert(END, name)

window.mainloop()