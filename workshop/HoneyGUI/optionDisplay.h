#ifndef HONEYGUI_OPTIONDISPLAY_H
#define HONEYGUI_OPTIONDISPLAY_H

#include <gtkmm.h>

class optionDisplay : public Gtk::Box { //Building a box to put the displays on
public:
    optionDisplay(); //Constructors
    virtual ~optionDisplay(); //Virtual Destrutor Man

protected: //TODO look into specific classes for each display
    void botStart(); //Starting the bot
    void botStop(); //Stopping it

    Gtk::Box statusDisplay; //The display for status
    Gtk::Button m_button1, m_button2; //Buttons!
};


#endif //HONEYGUI_OPTIONDISPLAY_H
