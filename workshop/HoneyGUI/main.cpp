#include "guiBase.h"
#include <iostream>

//To manually build, run 'g++ -o test main.cpp guiBase.cpp controlDisplay.cpp configDisplay.cpp pluginDisplay.cpp $(pkg-config gtkmm-3.0 --cflags --libs)'

int main(int argc, char *argv[]) {
    system("x=$(find ~/ -name \"honeybot\" | head -n 1); echo $x > path.txt");
    system("x=$(find ~/ -name \"honeybot\" | head -n 1); cd $x/honeybot/plugins; ls > plugins.txt");

    auto app = Gtk::Application::create(argc, argv, "org.gtkmm.example"); //Simply creates the application window to run
    //everything in

    guiBase window;

    return app->run(window); //Starts the runtime loop for GTK
}
