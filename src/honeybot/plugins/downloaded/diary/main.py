"""
[diary.py]
Diary Plugin

[Author]
Angelo Giacco

[About]
Keeps a record of your diary

[Commands]
>>>.diary record <diary entry>
Adds to that day's diary entry

>>>.diary show <date>
Will show the diary entry of specified date (can also accept "today", "yesterday")

>>>.diary delete
Will delete today's entry

>>>.diary help
Gives help about how to use the plugin
"""

import os
from datetime import datetime, timedelta

if not os.path.exists("diary"):
    """create diary folder"""

    try:
        os.mkdir("diary")
    except Exception as e:
        print("Something went wrong in diary plugin " + str(e))


class Plugin:
    def __init__(self):
        pass

    def today_yesterday(self, date):
        if date == "today":
            date = datetime.today().strftime("%d-%m-%Y")
        elif date == "yesterday":
            date = datetime.strftime(datetime.now() - timedelta(1), "%d-%m-%Y")
        return date

    def get_path(self, time):
        """get path for diary entry from timestamp"""

        date_obj = datetime.fromtimestamp(time)
        date = date_obj.strftime("%d-%m-%Y")
        path = "diary/" + date
        return path

    def record(self, time, text):
        """adds to existing entry or creates new one"""

        path = Plugin.get_path(self, time)
        if not os.path.exists(path):
            with open(path, "w+") as file:
                content = " ".join(text)
                file.write(content)
                return False
        else:
            with open(path, "a") as file:
                content = " ".join(text)
                file.write(content)
                return True

    def get_record(self, date):
        """
        check if there is a diary entry for a certain date and return it if there is
        """
        date = Plugin.today_yesterday(self, date)
        path = "diary/" + date
        if not os.path.exists(path):
            return [
                "There is no diary entry for that date.",
                "Check the date is entered correctly!",
            ]
        else:
            with open(path) as file:
                entry = file.readlines()
            print([x.strip("\n") for x in entry])
            return [x.strip("\n") for x in entry]

    def delete(self, time):
        """check if entry exists and if it does delete it"""
        path = Plugin.get_path(self, time)
        if not os.path.exists(path):
            return "There is no diary entry for that date. Check the date is entered correctly!"
        else:
            os.remove(path)
            return "Entry deleted successfully!"

    def run(self, incoming, methods, info, bot_info):
        try:
            owner = bot_info["owners"]
            time = bot_info["time"]
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".diary":
                index = info["prefix"].find("!")
                name = info["prefix"][:index]
                if name not in owner:
                    methods["send"](info["address"], "Access denied! You are not the owner!")
                else:

                    if msgs[1].lower() == "delete":
                        if len(msgs) != 2:
                            methods["send"](info["address"], "Invalid input!")
                        else:
                            methods["send"](info["address"], Plugin.delete(self, time))

                    elif msgs[1].lower() == "show":
                        if len(msgs) != 3:
                            methods["send"](
                                info["address"],
                                "Invalid Input. Try .diary show 21-03-2020",
                            )
                        else:
                            for line in Plugin.get_record(self, msgs[2]):
                                methods["send"](info["address"], line)

                    elif msgs[1].lower() == "record":
                        if len(msgs) > 2:
                            flag = Plugin.record(
                                self, time, msgs[2:]
                            )  # will return true if there was already an entry
                            if flag:
                                methods["send"](
                                    info["address"],
                                    "Text added to diary entry successfully!",
                                )
                            else:
                                methods["send"](
                                    info["address"], "Diary entry created successfully!"
                                )
                        else:
                            methods["send"](info["address"], "No text to record.")

                    elif msgs[1].lower() == "help":
                        methods["send"](info["address"], "Try the following commands!")
                        methods["send"](info["address"], ".diary record this is an example ")
                        methods["send"](
                            info["address"],
                            ".diary show today or .diary show 01-01-2000",
                        )
                        methods["send"](info["address"], ".diary delete")
                        methods["send"](info["address"], "That's all there is to this plugin!")

        except Exception as e:
            print("woops, diary plugin error", e)
