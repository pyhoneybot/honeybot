/**
 * The screen to display the plugin select
 */

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
    void alterCheck(bool yes, std::string plu); //Alters the check string
    void savePlug(); //Connects the save button
    int fileSave(); //Save the check string to PLUGINS.conf
    int get_list(); //Gets the currently selected plugins

    std::string path; //The path to honeybot
    std::string checks; //The string to save all the selected plugins to for easy file writing
    std::vector<std::string> plugins; //All the available plugins
    std::vector<std::string> stdPlugins; //Vector of standard plugins
    std::vector<std::string> selected; //Vector of the plugins INITIALLY selected

    Gtk::Alignment alignment1;
    Gtk::Paned plugPane; //The pane to seperate save and select
    Gtk::Button save; //The save button
    Gtk::ScrolledWindow scroll; //The select screen
    Gtk::ButtonBox plugs; //The box where the plugins are stored
    std::array <Gtk::CheckButton, 100> butts; //Yay easily CheckButton creation
};


#endif //HONEYGUI_PLUGINDISPLAY_H
