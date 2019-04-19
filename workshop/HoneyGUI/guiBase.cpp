#include "guiBase.h"
#include <iostream>

guiBase::guiBase() : m_HPaned(Gtk::ORIENTATION_HORIZONTAL), m_VPaned(Gtk::ORIENTATION_VERTICAL) {
    set_title("HoneyGUI"); //Sets the title for the project
    set_border_width(10); //Default border width
    set_default_size(1200, 400); //Window size TODO make window more adjustable

    add(m_HPaned); //Adds the paned view

    m_VPaned.add1(controls); //Adding in the control panel to the top left
    m_VPaned.add2(config); //Adding in the config editor to the bottom right

    m_VPaned.set_position(100); //Setting the left divider

    m_HPaned.add1(m_VPaned); //Adding the left side
    m_HPaned.add2(plugins); //Adding plugin select to the right

    m_HPaned.set_position(800); //This is the horizontal divider TODO make horizontal divider auto-adjust

    show_all_children(); //Exactly what it sounds like
}

guiBase::~guiBase() {} //Yay easy virtual destructor so the deletion and garbage collection isn't completely trash! This
//sets it so that the objects of the m_HPaned are deleted from the bottom up, not from the base and have a bunch of
//scary wild pointers
