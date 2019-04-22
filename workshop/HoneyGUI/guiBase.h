/**
 * Easy way to connect everything and organize
 */

#ifndef HONEYGUI_GUIBASE_H
#define HONEYGUI_GUIBASE_H

#include <gtkmm.h>
#include "controlDisplay.h"
#include "configDisplay.h"
#include "pluginDisplay.h"

class guiBase : public Gtk::Window { //Creates the window and such
public:
    guiBase(); //Automagical constructor
    virtual ~guiBase(); //Virtual destructor

protected:
    Gtk::Paned m_HPaned; //The main paned container
    Gtk::Paned m_VPaned; //The left side of the screen
    controlDisplay controls; //Controls Display
    configDisplay config; //Config Editor Display
    pluginDisplay plugins; //Plugin Select Display
};


#endif //HONEYGUI_GUIBASE_H
