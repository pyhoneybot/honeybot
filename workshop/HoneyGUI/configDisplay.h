#ifndef HONEYGUI_CONFIGDISPLAY_H
#define HONEYGUI_CONFIGDISPLAY_H

#include <gtkmm.h>
#include <string>

class configDisplay : public Gtk::Frame {
public:
    configDisplay();
    virtual ~configDisplay();

protected:
    std::string path;

    int file_replace(std::string toReplace, std::string replaceWith, std::string file);
    int file_seperated(std::string write, std::string file);
    void on_entry_activated(Gtk::Entry* text, const std::string& change, std::string file);
    void seperated_entry_activated(Gtk::Entry* text, std::string change, std::string file);

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
