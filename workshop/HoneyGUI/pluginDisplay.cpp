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

pluginDisplay::pluginDisplay() : plugPane(Gtk::ORIENTATION_VERTICAL), plugs(Gtk::ORIENTATION_VERTICAL) {
    std::ifstream infile;
    infile.open("path.txt");
    getline(infile, path);
    infile.close();

    path += "/honeybot/";

    infile.open(path + "plugins/plugins.txt");
    std::string strTemp;

    while (getline(infile, strTemp)){
        if(strTemp.substr(strTemp.length() - 3) == ".py") {
            plugins.push_back(strTemp.substr(0, strTemp.length() - 3));
        }
    }

    infile.close();
    infile.open(path + "plugins/plugins.txt");

    while (getline(infile, strTemp)){
        if(strTemp.substr(strTemp.length() - 3) == ".py") {
            plugins.push_back(strTemp.substr(0, strTemp.length() - 3));
        }
    }

    infile.close();
    infile.open(path + "settings/STD_PLUGINS.conf");

    while (getline(infile, strTemp)) {
        stdPlugins.push_back(strTemp);
    }

    infile.close();

    for (int i = 0; i < plugins.size(); ++i) {
        plugs.pack_start(butts[i]);

        strTemp = "User Plugin";

        if (std::find(stdPlugins.begin(), stdPlugins.end(), plugins[i]) != stdPlugins.end()){
            strTemp = "Standard Plugin";
        }

        butts[i].set_label(plugins[i] + " | " + strTemp);
        butts[i].signal_toggled().connect( sigc::bind(sigc::mem_fun(*this, &pluginDisplay::alterCheck), butts[i].property_active(), plugins[i]) );
    }

    scroll.add(plugs);

    scroll.set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_ALWAYS);

    plugPane.add1(scroll);
    plugPane.add2(save);
    plugPane.set_position(325);

    save.set_label("Save");
    save.signal_clicked().connect( sigc::mem_fun(*this, &pluginDisplay::savePlug) );

    alignment1.add(plugPane);

    add(alignment1);
    set_label("Plugins");

    show_all_children();
}

pluginDisplay::~pluginDisplay() {}

void pluginDisplay::alterCheck(bool yes, std::string plu) {
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