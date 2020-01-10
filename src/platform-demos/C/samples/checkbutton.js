#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const CheckButtonExample = new Lang.Class({
    Name: 'CheckButton Example',

    // Create the application itself
    _init: function() {
        this.application = new Gtk.Application({
            application_id: 'org.example.jscheckbutton',
            flags: Gio.ApplicationFlags.FLAGS_NONE
        });

    // Connect 'activate' and 'startup' signals to the callback functions
    this.application.connect('activate', Lang.bind(this, this._onActivate));
    this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents window when active
    _onActivate: function() {
        this._window.present();
    },

    // Callback function for 'startup' signal builds the UI
    _onStartup: function() {
        this._buildUI ();
    },



    // Build the application's UI
    _buildUI: function() {

        // Create the application window
        this._window = new Gtk.ApplicationWindow({
            application: this.application,
            window_position: Gtk.WindowPosition.CENTER,
            default_height: 100,
            default_width: 300,
            border_width: 10,
            title: "CheckButton Example"});

        // Create the check button
        this._button = new Gtk.CheckButton ({label: "Show Title"});
        this._window.add (this._button);

        // Have the check button be checked by default
        this._button.set_active (true);

        // Connect the button to a function that does something when it's toggled
        this._button.connect ("toggled", Lang.bind (this, this._toggledCB));

        // Show the window and all child widgets
        this._window.show_all();
    },



    _toggledCB: function () {

        // Make the window title appear or disappear when the checkbox is toggled
        if (this._button.get_active() == true)
            this._window.set_title ("CheckButton Example");
        else
            this._window.set_title ("");

    }

});

// Run the application
let app = new CheckButtonExample ();
app.application.run (ARGV);
