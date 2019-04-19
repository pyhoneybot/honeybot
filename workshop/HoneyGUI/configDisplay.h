#ifndef HONEYGUI_CONFIGDISPLAY_H
#define HONEYGUI_CONFIGDISPLAY_H

#include <gtkmm.h>

class configDisplay : public Gtk::Frame {
public:
    configDisplay();
    virtual ~configDisplay();

protected:
    Gtk::Alignment alignment1;
    Gtk::Grid editors;

    Gtk::Frame nameFrame; //All the frames and editors to make everything legible
    Gtk::Entry nameEntry;
    Gtk::Frame serverFrame;
    Gtk::Entry serverEntry;
    Gtk::Frame portFrame;
    Gtk::Entry portEntry;
    Gtk::Frame channelFrame;
    Gtk::Entry channelEntry;
    Gtk::Frame euserFrame; //All email config stuff
    Gtk::Entry euserEntry;
    Gtk::Frame epassFrame;
    Gtk::Entry epassEntry;
    Gtk::Frame eservFrame;
    Gtk::Entry eservEntry;
    Gtk::Frame eportFrame;
    Gtk::Entry eportEntry;
};


#endif //HONEYGUI_CONFIGDISPLAY_H
