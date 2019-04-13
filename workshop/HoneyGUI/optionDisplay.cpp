#include "optionDisplay.h"
#include <iostream>

optionDisplay::optionDisplay() {
    set_border_width(10); //More default border

    statusDisplay.pack_start(m_button1); //Shoving everything into a box and leaving it to die...
    statusDisplay.pack_start(m_button2);

    m_button1.add_label("Start Bot"); //Naming the buttons
    m_button2.add_label("Stop Bot");

    m_button1.set_size_request(100, 50); //A bunch of terrible code to make the buttons remotely pleasing
    m_button1.set_border_width(25); //TODO fix this god awful mess and unfrankenstein your code
    m_button1.set_margin_bottom(680);
    m_button2.set_size_request(100, 50);
    m_button2.set_border_width(25);
    m_button2.set_margin_bottom(680);

    m_button1.signal_clicked().connect( sigc::mem_fun(*this, &optionDisplay::botStart) ); //Connecting the actions to
    m_button2.signal_clicked().connect( sigc::mem_fun(*this, &optionDisplay::botStop) ); //the buttons

    add(statusDisplay); //Putting all of this onto the screen

    show_all_children(); //SHOW ME YOUR CHILD
}

optionDisplay::~optionDisplay() {} //More virtual destruction!

void optionDisplay::botStart() { //This is to execute the Python script...
    std::cout << "Starting the bot..." << std::endl;
    system("cd ./../../honeybot; nohup python3 main.py&");
}

void optionDisplay::botStop() { //...and this is to put a bullet in it
    std::cout << "Stopping the bot..." << std::endl;
    system("pkill -f main.py");
}