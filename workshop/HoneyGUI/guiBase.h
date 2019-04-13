#ifndef HONEYGUI_GUIBASE_H
#define HONEYGUI_GUIBASE_H

#include <gtkmm.h>
#include "optionList.h"
#include "optionDisplay.h"

class guiBase : public Gtk::Window { //Creates the window and such
public:
    guiBase(); //Automagical constructor
    virtual ~guiBase(); //Virtual destructor

protected:
    Gtk::Paned m_HPaned; //The paned container
    optionList m_OptionsList; //The options list
    optionDisplay m_OptionsDisplay; //The options display
};


#endif //HONEYGUI_GUIBASE_H
