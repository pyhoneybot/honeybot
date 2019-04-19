#include "configDisplay.h"

configDisplay::configDisplay() {
    editors.set_column_spacing(10); //Some visually appealing stuff
    editors.set_row_spacing(10);
    editors.set_margin_left(10);
    editors.set_margin_top(5);

    editors.attach(nameFrame, 0, 0, 2, 1); //Adding in all the frames and entries
    nameFrame.set_label("Bot Name");
    nameFrame.add(nameEntry);

    editors.attach(serverFrame, 0, 1, 1, 1);
    serverFrame.set_label("Server URL");
    serverFrame.add(serverEntry);

    editors.attach(portFrame, 1, 1, 1, 1);
    portFrame.set_label("Port Number");
    portFrame.add(portEntry);

    editors.attach(channelFrame, 2, 1, 1, 1);
    channelFrame.set_label("Channels, Comma Seperated");
    channelFrame.add(channelEntry);

    editors.attach(euserFrame, 0, 2, 1, 1);
    euserFrame.set_label("Email");
    euserFrame.add(euserEntry);

    editors.attach(epassFrame, 1, 2, 1, 1);
    epassFrame.set_label("Email Password");
    epassFrame.add(epassEntry);

    editors.attach(eservFrame, 2, 2, 1, 1);
    eservFrame.set_label("SMTP Server");
    eservFrame.add(eservEntry);

    editors.attach(eportFrame, 3, 2, 1, 1);
    eportFrame.set_label("SMTP Port");
    eportFrame.add(eportEntry);

    //TODO connect all the entry activated signals

    alignment1.add(editors);

    add(alignment1);
    set_label("Config");

    show_all_children();
}

configDisplay::~configDisplay() {}