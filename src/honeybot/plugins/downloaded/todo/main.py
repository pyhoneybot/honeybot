# -*- coding: utf-8 -*-
"""
[todo.py]
Todo list Plugin

[Author]
Himanshu Ranjan

[Website]
https://github.com/h-ranjan1110

[About]
Todo list keeps all your pending task .
You can add a task ,delete or show list.
This list is stored in a text file called todo.txt in honeybot directory.
If this does not exist it creates one.

[Commands]
>>>.todo add <Your Task Here>
It adds the task to do the todo list.

>>>.todo delete <index>
To delete a task input it's index number as shown in the list.

>>>.todo show
It shows all the task currently on the list.

>>>.todo clear
This will delete all the task in the list.

>>>.todo help
sends messages explaining how to use the todo plugin
"""

import os

if not os.path.exists("todo.txt"):
    """ Creating todo.txt is it is not already present. """
    todo = open("todo.txt", "w+")
    todo.close()


class Plugin:
    def __init__(self):
        pass

    def get_help(info, methods):
        """ help function to give information about commands."""
        methods["send"](
            info["address"],
            ".todo add  <Your Task Here> \
            (It adds the task to do the todo list.)",
        )
        methods["send"](
            info["address"],
            ".todo delete  <index> \
            (To delete a task input it's index number as shown in the list.)",
        )
        methods["send"](
            info["address"],
            ".todo show \
            (It shows all the task currently on the list.)",
        )
        methods["send"](
            info["address"],
            ".todo clear \
            (This will delete all the task in the list.)",
        )
        methods["send"](
            info["address"],
            ".todo help \
            (sends messages explaining how to use the todo plugin.)",
        )

    def showlist(info, methods):
        """ It prints the todo file on the screen """
        # Parse the user ID from info['prefix']
        raw_user = info["prefix"]
        user_index = raw_user.find("!")
        user = raw_user[0:user_index]

        if os.stat("todo.txt").st_size == 0:
            methods["send"](
                info["address"], "Awesome " + user + ". You Have No Task Pending!"
            )
        else:
            methods["send"](info["address"], "Hi, " + user + ". These are your tasks.")
            with open("todo.txt", "r") as f:
                lines = f.readlines()
            count = 1
            for line in lines:
                methods["send"](info["address"], str(count) + ". " + line)
                count = count + 1

    def run(self, incoming, methods, info, bot_info):
        """ Handling of requests from user."""
        try:
            msgs = info["args"][1:][0].split()

            if info["command"] == "PRIVMSG" and msgs[0] == ".todo":

                # adding new task to beginning of list
                if msgs[1] == "add":
                    task_start_index = 9
                    task = info["args"][1:][0][task_start_index:]
                    with open("todo.txt", "r+") as todo:
                        content = todo.read()
                        todo.seek(0, 0)
                        todo.write(task.rstrip("\n") + "\n" + content)
                    Plugin.showlist(info, methods)

                # deleting the line of given index
                elif msgs[1] == "delete":
                    line_no = int(msgs[2])

                    with open("todo.txt", "r") as f:
                        lines = f.readlines()

                    count = 1
                    with open("todo.txt", "w") as f:
                        for line in lines:
                            if count != line_no:
                                f.write(line)
                            count = count + 1
                    Plugin.showlist(info, methods)

                # Deleting all the task . todo.txt file is not deleted
                elif msgs[1] == "clear":
                    open("todo.txt", "w").close()
                    Plugin.showlist(info, methods)

                # Displaying all task in file .
                elif msgs[1] == "show":
                    Plugin.showlist(info, methods)

                # Showing help
                elif msgs[1] == "help":
                    Plugin.get_help(info, methods)
                else:
                    methods["send"](info["address"], "Please Select A Valid Option")

        except Exception as e:
            print("woops plugin", __file__, e)
