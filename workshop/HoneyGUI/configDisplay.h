/**
 * This displays the config editor using multiple Gtk::Entry widgets
 */

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

    int file_replace(std::string toReplace, std::string replaceWith, std::string file); //Replaces the config field
    int file_seperated(std::string write, std::string file); //Writes a string with newline characters to a conf file
    std::string get_conf(std::string field, std::string file); //Gets the conf field specified
    std::string get_list(std::string file); //Gets the entirety of the conf file
    void on_entry_activated(Gtk::Entry* text, const std::string& change, std::string file); //Allows the signal to be connected to the file_replace
    void seperated_entry_activated(Gtk::Entry* text, std::string change, std::string file); //Allows the signal to be connected to the file_seperated

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
