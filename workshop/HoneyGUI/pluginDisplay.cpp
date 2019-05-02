#include "pluginDisplay.h"
#include <iostream>
#include <fstream>
#include <string>

int pluginDisplay::fileSave() {
    std::ofstream fileout1(path + "settings/PLUGINS.conf");
    if (!fileout1){
        std::cout << "File not found" << std::endl;
        return 1;
    }

    fileout1.clear();
    fileout1 << checks;
    fileout1.close();

    return 0;
}

int pluginDisplay::get_list() {
    std::ifstream infile(path + "settings/PLUGINS.conf");

    if(!infile){
        return 1;
    }

    std::string strTemp;

    while (getline(infile, strTemp)){
        checks += strTemp + '\n';
        selected.push_back(strTemp);
    }

    infile.close();

    return 0;
}

pluginDisplay::pluginDisplay() : plugPane(Gtk::ORIENTATION_VERTICAL), plugs(Gtk::ORIENTATION_VERTICAL) {
    std::ifstream infile; //Reading the path
    infile.open("path.txt");
    getline(infile, path);
    infile.close();

    path += "/honeybot/";
    std::string strTemp;

    infile.open(path + "plugins/plugins.txt");

    while (getline(infile, strTemp)){ //Reading the available plugins
        plugins.push_back(strTemp.substr(0, strTemp.length() - 3));
    }

    infile.close();

    get_list(); //Getting the selected plugins

    for (int i = 0; i < plugins.size(); ++i) { //Creating each CheckButton
        plugs.pack_start(butts[i]); //Adding it into view

        if (std::find(selected.begin(), selected.end(), plugins[i]) != selected.end()){
            butts[i].set_active(true); //If its preselected than activate it
        }

        butts[i].set_label(plugins[i]); //Setting the label
        butts[i].signal_toggled().connect( sigc::bind(sigc::mem_fun(*this, &pluginDisplay::alterCheck), butts[i].property_active(), plugins[i]) ); //Connecting the signal
    }

    scroll.add(plugs); //Adding in the button box

    scroll.set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_ALWAYS); //Rules for the scrollbar

    plugPane.add1(scroll); //Adding the scroll window
    plugPane.add2(save); //Adding the save button
    plugPane.set_position(325); //Manually setting the divider

    save.set_label("Save"); //Save button label
    save.signal_clicked().connect( sigc::mem_fun(*this, &pluginDisplay::savePlug) ); //Connecting the save button

    alignment1.add(plugPane); //Adding it all to the alignment

    add(alignment1);
    set_label("Plugins");

    show_all_children();
}

pluginDisplay::~pluginDisplay() {}

void pluginDisplay::alterCheck(bool yes, std::string plu) { //If ACTIVE add to checks otherwise remove from checks
    if (yes) {
        checks += plu + '\n';
    } else {
        int startPos = checks.find(plu + '\n');
        checks.erase(startPos, plu.size() + 1);
    }
}

void pluginDisplay::savePlug() {
    fileSave();
}