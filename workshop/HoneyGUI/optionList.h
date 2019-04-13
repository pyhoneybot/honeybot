#ifndef HONEYGUI_OPTIONLIST_H
#define HONEYGUI_OPTIONLIST_H


#include <gtkmm.h>

class optionList : public Gtk::ScrolledWindow { //Creates a scrollable window
public:
    optionList(); //The creator
    virtual ~optionList(); //and ender

    class ModelColumns : public Gtk::TreeModel::ColumnRecord { //This is how the columns for TreeView is made
    public:
        ModelColumns(){
            add(m_col_text);
        }

        Gtk::TreeModelColumn<Glib::ustring> m_col_text;
    };

    ModelColumns m_Columns;

protected:
    void gtk_tree_view_row_activated(); //Non functional code

    Glib::RefPtr<Gtk::ListStore> m_refListStore; //The ListStore
    Gtk::TreeView m_TreeView; //The TreeView
};


#endif //HONEYGUI_OPTIONLIST_H
