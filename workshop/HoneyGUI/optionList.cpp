#include "optionList.h"
#include <iostream>
#include <sstream>
#include <array>


optionList::optionList() {
    set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_AUTOMATIC); //Set whether the scrollbar should be on or not

    add(m_TreeView); //Putting the TreeView on the display

    m_refListStore = Gtk::ListStore::create(m_Columns); //Creating a ListStore of m_Columns

    m_TreeView.set_model(m_refListStore); //Setting the type of TreeView
    m_TreeView.set_activate_on_single_click(true); //This allows it to activate on a single click for toggling

    //Potential way to change the display
    //m_TreeView.signal_row_activated().connect(sigc::mem_fun(*this, &optionList::gtk_tree_view_row_activated));

    std::array<Glib::ustring, 3> options = {"Status", "Plugins", "Config"}; //All of our different options

    for(const auto & option : options) { //This is just displaying the options
        std::ostringstream text;
        text << option;

        Gtk::TreeModel::Row row = *(m_refListStore->append());
        row[m_Columns.m_col_text] = text.str();
    }

    m_TreeView.append_column("Options", m_Columns.m_col_text); //Adding in a nice lil' column

    show_all_children(); //GIVE ME MORE KINDERLINGS
}

optionList::~optionList() {} //EXTERMINATE

void optionList::gtk_tree_view_row_activated() { //Non functioning code...
    std::cout << "A row has been selected" << std::endl;
}