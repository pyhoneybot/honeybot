#include "configDisplay.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <regex>

int configDisplay::file_replace(std::string toReplace, std::string replaceWith, std::string file) {
    std::ifstream filein1(path + "/" + file);
    std::ofstream fileout1(path + "/temp.txt");

    if(!filein1 || !fileout1){
        std::cout << "Files not found" << std::endl;
        return 1;
    }

    fileout1.clear();

    std::string strTemp;
    std::regex match ("(" + toReplace + ")(.*)");

    while (getline(filein1, strTemp)){
        if (std::regex_match(strTemp, match)){
            strTemp = replaceWith;
        }

        strTemp += "\n";
        fileout1 << strTemp;
    }

    filein1.close(); fileout1.close();

    std::ifstream filein2(path + "/temp.txt");
    std::ofstream fileout2(path + "/" + file);

    fileout2.clear();

    while (getline(filein2, strTemp)) {
        fileout2 << strTemp + "\n";
    }

    filein2.close(); fileout2.close();

    system("x=$(find ~/ -name \"honeybot\" | head -n 1); rm $x/honeybot/settings/temp.txt");

    return 0;
}

int configDisplay::file_seperated(std::string write, std::string file) {
    std::ofstream fileout1(path + "/" + file);
    if (!fileout1){
        std::cout << "File not found" << std::endl;
        return 1;
    }

    fileout1.clear();
    fileout1 << write;
    fileout1.close();

    return 0;
}

std::string configDisplay::get_conf(std::string field, std::string file) {
    std::ifstream infile(path + "/" + file);

    if(!infile){
        return "";
    }

    std::string strTemp;
    std::regex match ("(" + field + ")(.*)");

    while (getline(infile, strTemp)){
        if (std::regex_match(strTemp, match)){
            return strTemp.erase(0, field.length());
        }
    }

    infile.close();
}

std::string configDisplay::get_list(std::string file) {
    std::ifstream infile(path + "/" + file);

    if(!infile){
        return "";
    }

    std::string strTemp;
    std::string x;

    while (getline(infile, strTemp)){
        x += strTemp + ", ";
    }

    infile.close();

    return x;
}

configDisplay::configDisplay() {
    std::ifstream infile;
    infile.open("path.txt");
    getline(infile, path);
    infile.close();

    path += "/honeybot/settings";

    editors.set_column_spacing(10); //Some visually appealing stuff
    editors.set_row_spacing(10);
    editors.set_margin_left(10);
    editors.set_margin_top(5);

    editors.attach(nameFrame, 0, 0, 2, 1); //Adding in all the frames and entries, along with their properties
    nameFrame.set_label("Bot Name");
    nameFrame.add(nameEntry);
    nameEntry.set_text(get_conf("name = ", "CONNECT.conf"));
    nameEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &nameEntry, "name = ", "CONNECT.conf") );

    editors.attach(serverFrame, 0, 1, 1, 1);
    serverFrame.set_label("Server URL");
    serverFrame.add(serverEntry);
    serverEntry.set_text(get_conf("server_url = ", "CONNECT.conf"));
    serverEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &serverEntry, "server_url = ", "CONNECT.conf") );

    editors.attach(portFrame, 1, 1, 1, 1);
    portFrame.set_label("Port Number");
    portFrame.add(portEntry);
    portEntry.set_text(get_conf("port = ", "CONNECT.conf"));
    portEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &portEntry, "port = ", "CONNECT.conf") );

    editors.attach(channelFrame, 2, 1, 1, 1);
    channelFrame.set_label("Channels, Comma Seperated");
    channelFrame.add(channelEntry);
    channelEntry.set_text(get_list("AUTOJOIN_CHANNELS.conf"));
    channelEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::seperated_entry_activated), &channelEntry, "", "AUTOJOIN_CHANNELS.conf") );

    editors.attach(euserFrame, 0, 2, 1, 1);
    euserFrame.set_label("Email");
    euserFrame.add(euserEntry);
    euserEntry.set_text(get_conf("Email: ", "email_config.conf"));
    euserEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &euserEntry, "Email: ", "email_config.conf") );

    editors.attach(epassFrame, 1, 2, 1, 1);
    epassFrame.set_label("Email Password");
    epassFrame.add(epassEntry);
    epassEntry.set_visibility(false);
    epassEntry.set_text(get_conf("Password: ", "email_config.conf"));
    epassEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &epassEntry, "Password: ", "email_config.conf") );

    editors.attach(eservFrame, 2, 2, 1, 1);
    eservFrame.set_label("SMTP Server");
    eservFrame.add(eservEntry);
    eservEntry.set_text(get_conf("SMTP Server: ", "email_config.conf"));
    eservEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &eservEntry, "SMTP Server: ", "email_config.conf") );

    editors.attach(eportFrame, 3, 2, 1, 1);
    eportFrame.set_label("SMTP Port");
    eportFrame.add(eportEntry);
    eportEntry.set_text(get_conf("SMTP Server Port: ", "email_config.conf"));
    eportEntry.signal_activate().connect( sigc::bind<Gtk::Entry*>(sigc::mem_fun(*this, &configDisplay::on_entry_activated), &eportEntry, "SMTP Server Port: ", "email_config.conf") );

    alignment1.add(editors);

    add(alignment1);
    set_label("Config");

    show_all_children();
}

configDisplay::~configDisplay() {}

void configDisplay::on_entry_activated(Gtk::Entry* text, const std::string& change, std::string file) {
    configDisplay::file_replace(change, change + text->get_text().c_str(), file);
}

void configDisplay::seperated_entry_activated(Gtk::Entry *text, std::string change, std::string file) {
    std::string sep = text->get_text().c_str();

    sep.erase(remove_if(sep.begin(), sep.end(), ::isspace), sep.end());
    std::replace(sep.begin(), sep.end(), ',', '\n');

    configDisplay::file_seperated(sep, file);
}