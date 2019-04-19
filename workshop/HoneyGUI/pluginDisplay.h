//
// Created by erev on 4/19/19.
//

#ifndef HONEYGUI_PLUGINDISPLAY_H
#define HONEYGUI_PLUGINDISPLAY_H

#include <gtkmm.h>

class pluginDisplay : public Gtk::Frame {
public:
    pluginDisplay();
    virtual ~pluginDisplay();

protected:
    Gtk::Alignment alignment1;
};


#endif //HONEYGUI_PLUGINDISPLAY_H
