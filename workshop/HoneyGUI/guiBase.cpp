#include "guiBase.h"

guiBase::guiBase() : m_HPaned(Gtk::ORIENTATION_HORIZONTAL) {
    set_title("HoneyGUI"); //Sets the title for the project
    set_border_width(10); //Default border width
    set_default_size(1400, 800); //Window size TODO make window more adjustable

    add(m_HPaned); //Adds the paned view

    m_HPaned.add1(m_OptionsList); //Adds the options list TODO figure out how to get these to interact
    m_HPaned.add2(m_OptionsDisplay); //Adds the display options

    m_HPaned.set_position(400); //This is the vertical divider TODO make vertical divider auto-adjust

    show_all_children(); //Exactly what it sounds like
}

guiBase::~guiBase() {} //Yay easy virtual destructor so the deletion and garbage collection isn't completely trash! This
//sets it so that the objects of the m_HPaned are deleted from the bottom up, not from the base and have a bunch of
//scary wild pointers
