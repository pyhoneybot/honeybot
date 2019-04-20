#include "pluginDisplay.h"

pluginDisplay::pluginDisplay() {
    add(alignment1); //TODO actually add this in
    set_label("Plugins");

    show_all_children();
}

pluginDisplay::~pluginDisplay() {}