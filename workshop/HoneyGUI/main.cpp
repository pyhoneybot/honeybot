#include "guiBase.h"
#include <iostream>

/**
 * To properly use, have Gtkmm-3.0 or better installed, and g++ (or any compiler if you're experienced)
 *
 * To download Gtkmm, first download Gtk following https://www.gtk.org/download/index.php along with all dependencies
 * Next, install following  https://developer.gnome.org/gtkmm-tutorial/stable/chapter-installation.html.en
 *
 * In essence, on Linux, run
 *      Debian: sudo apt-get install libgtkmm-3.0-dev
 *      Redhat: sudo dnf install gtkmm30-devel
 *
 * To manually build, run 'g++ -o test main.cpp guiBase.cpp controlDisplay.cpp configDisplay.cpp pluginDisplay.cpp $(pkg-config gtkmm-3.0 --cflags --libs)'
 */

int main(int argc, char *argv[]) {
    system("x=$(find ~/ -name \"honeybot\" | head -n 1); echo $x > path.txt"); //Finds the path to honeybot and outputs it to a file for easy access
    system("x=$(find ~/ -name \"honeybot\" | head -n 1); cd $x/honeybot/plugins; ls *.py > plugins.txt"); //Outputs all available plugins for pluginDisplay

    auto app = Gtk::Application::create(argc, argv, "org.gtkmm.example"); //Simply creates the application window to run
    //everything in

    guiBase window;

    return app->run(window); //Starts the runtime loop for GTK
}
