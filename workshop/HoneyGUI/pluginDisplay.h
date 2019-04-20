#ifndef HONEYGUI_PLUGINDISPLAY_H
#define HONEYGUI_PLUGINDISPLAY_H

#include <gtkmm.h>
#include <string>
#include <vector>
#include <array>

class pluginDisplay : public Gtk::Frame {
public:
    pluginDisplay();
    virtual ~pluginDisplay();

protected:
    void alterCheck(bool yes, std::string plu);
    void savePlug();
    int fileSave();

    std::string path;
    std::string checks;
    std::vector<std::string> plugins;
    std::vector<std::string> stdPlugins;

    Gtk::Alignment alignment1;
    Gtk::Paned plugPane;
    Gtk::Button save;
    Gtk::ScrolledWindow scroll;
    Gtk::ButtonBox plugs;
    std::array <Gtk::CheckButton, 100> butts;
};


#endif //HONEYGUI_PLUGINDISPLAY_H
