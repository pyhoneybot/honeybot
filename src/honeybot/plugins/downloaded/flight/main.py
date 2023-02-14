"""
[flight.py]
Flight information plugin

[Author]
Angelo Giacco

[About]
returns flight information

[Commands]
>>> .flight <<flight callsign>>
"""

import flightradar24 as fr24


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1].split()[0] == ".flight":

                if len(info["args"][1].split()) != 2:  # check only callsign provided
                    methods["send"](
                        info["address"],
                        "Invalid input. Ensure callsign has no spaces. Try .ba778",
                    )

                else:
                    fr = fr24.Api()
                    id = info["args"][1].split()[1]
                    flight = fr.get_flight(id)

                    if "errors" in flight:  # check for api error
                        methods["send"](
                            info["address"],
                            "Invalid input! Callsign " + "should not be more than 10 characters!",
                        )

                    else:
                        count = flight["result"]["response"]["item"][
                            "current"
                        ]  # get how many flights are recorded with callsign
                        if count == 0:
                            methods["send"](
                                info["address"],
                                "There are no flights with a corresponding callsign!",
                            )

                        else:
                            origin = flight["result"]["response"]["data"][0]["airport"]["origin"][
                                "position"
                            ]["region"]["city"]
                            destination = flight["result"]["response"]["data"][0]["airport"][
                                "destination"
                            ]["position"]["region"]["city"]
                            methods["send"](
                                info["address"],
                                "Flight " + id + " is from " + origin + " to " + destination + ".",
                            )

                            total = 0
                            count = 0
                            for f in flight["result"]["response"][
                                "data"
                            ]:  # flight["result"]["response"]["data"]
                                # will hold a week long history of flights
                                if f["status"]["live"]:
                                    methods["send"](
                                        info["address"],
                                        "This flight is currently in the air. "
                                        + "The following information is available:",
                                    )
                                    methods["send"](info["address"], f["status"]["text"])

                                if f["time"]["other"]["duration"] is not None:
                                    total += f["time"]["other"]["duration"]
                                    count += 1

                            avgDuration = total / count
                            mins = int(5 * round(float(avgDuration) / 5))  # round to nearest five
                            hours = 0
                            while avgDuration >= 60:
                                mins -= 60
                                hours += 1

                            methods["send"](
                                info["address"],
                                "The flight has an average duration of "
                                + str(hours)
                                + ":"
                                + str(mins)
                                + ".",
                            )

        except Exception as e:
            print("woops flight plugin error", e)
