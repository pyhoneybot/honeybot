from tkinter import *
import tkinter as tk
import os
import inspect
import configparser
import queue
import threading

window = tk.Tk()
window.geometry("650x670")
window.title("Manager")

current_path = os.path.split(os.path.abspath(__file__))[0]
pluginPath = os.path.join(os.sep, current_path, "plugins")
configPath = os.path.join(os.sep, current_path, "settings", "PLUGINS.conf")


def get_unique_text(text):
    uniques = sorted(set([i.strip() for i in text.split("\n") if i]))
    uniques_text = "\n".join(uniques)
    return uniques_text


def saveFile():
    text = tt.get(1.0, END)
    unique_text = get_unique_text(text)
    with open(configPath, "w+") as f:
        f.write(get_unique_text(unique_text))
    tt.delete(1.0, END)
    tt.insert(1.0, unique_text)


def reorder():
    text = tt.get(1.0, END)
    unique_text = get_unique_text(text)
    tt.delete(1.0, END)
    tt.insert(1.0, unique_text)


def getPlugins(dirName):
    listOfFile = os.listdir(dirName)
    return listOfFile


def clicked():
    selected = [listbox.get(pos) for pos in listbox.curselection()]
    for file in selected:
        tt.insert(END, file[:-3] + "\n")


rbot_thread = ""


def run_bot():
    global rbot_thread

    def run_it():
        exec(open("run.py").read())

    rbot_thread = threading.Thread(target=run_it)
    rbot_thread.start()
    runBot.config(state="disabled")
    stopBot.config(state="active")


def stop_bot():
    global rbot_thread
    rbot_thread.terminate()
    runBot.config(state="active")
    stopBot.config(state="disabled")


def exit_app(self):
    if messagebox.askokcancel("Quit", "Really quit?"):
        rbot_thread.terminate()
        window.destroy()


pluginList = getPlugins(pluginPath)

elements = [
    [
        [
            "MainLabel",
            Label(
                window,
                text="Select the plugins you wish to \
                        load and add them to the config file",
            ),
        ]
    ],
    [["listbox", Listbox(window, width=60)]],
    [["addBtn", Button(window, text="Add Plugin", width=10, command=clicked)]],
    [["label2", Label(window, text="Editable PLUGINS.conf file:")]],
    [["tt", Text(window, width=80)]],
    [["label3", Label(window, text="Don't forget to hit save!")]],
    [
        ["saveBtn", Button(
            window,
            text="Save File",
            width=10,
            command=saveFile)],
        ["reorderBtn", Button(
            window,
            text="Reorder",
            width=10,
            command=reorder)],
    ],
    [
        ["runBot", Button(window, text="RUN", width=10, command=run_bot)],
        ["stopBot", Button(window, text="STOP", width=10, command=stop_bot)],
    ],
]

for row_i, row in enumerate(elements):
    for col_i, col in enumerate(row):
        var_name = col[0]
        gui = col[1]
        _g = globals()
        _g[var_name] = gui
        if var_name in ["tt", "listbox", "addBtn"]:
            _g[var_name].grid(row=row_i, column=col_i, columnspan=2)
            window.grid_columnconfigure(col_i, weight=1, uniform="foo")
        else:
            _g[var_name].grid(row=row_i, column=col_i, sticky="NSEW")
            window.grid_columnconfigure(col_i, weight=1, uniform="foo")

tt.insert(END, open(configPath).read())

for name in pluginList:
    if name[-2:] == "py":
        listbox.insert(END, name)

window.mainloop()
window.protocol("WM_DELETE_WINDOW", exit_app)
