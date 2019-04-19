#include "controlDisplay.h"
#include <iostream>

controlDisplay::controlDisplay() : box1(Gtk::ORIENTATION_HORIZONTAL) {
    controls.set_margin_left(10);

    start.add_label("Start Bot");
    stop.add_label("Stop Bot");

    controls.pack_start(start);
    controls.pack_start(stop);

    box1.pack_start(controls);
    box1.pack_start(box2);

    alignment1.add(box1);

    add(alignment1);
    set_label("Controls");

    start.signal_clicked().connect( sigc::mem_fun(*this, &controlDisplay::botStart) );
    stop.signal_clicked().connect( sigc::mem_fun(*this, &controlDisplay::botStop) );

    show_all_children();
}

controlDisplay::~controlDisplay() {}

void controlDisplay::botStart() { //This is to execute the Python script...
    std::cout << "Starting the bot..." << std::endl;
    system("cd ./../../honeybot; nohup python3 main.py&");
}

void controlDisplay::botStop() { //...and this is to put a bullet in it
    std::cout << "Stopping the bot..." << std::endl;
    system("pkill -f main.py");
}