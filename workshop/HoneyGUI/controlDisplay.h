/**
 * This displays the basic bot controls
 */

#ifndef HONEYGUI_CONTROLDISPLAY_H
#define HONEYGUI_CONTROLDISPLAY_H

#include "gtkmm.h"

class controlDisplay : public Gtk::Frame {
public:
    controlDisplay();
    virtual ~controlDisplay();

protected:
    void botStart();
    void botStop();

    Gtk::Alignment alignment1;
    Gtk::Box box1; //TODO test with paned
    Gtk::Box box2;
    Gtk::ButtonBox controls;
    Gtk::Button start;
    Gtk::Button stop;
};


#endif //HONEYGUI_CONTROLDISPLAY_H
