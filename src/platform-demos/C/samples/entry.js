#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const EntryExample = new Lang.Class({
    Name: 'Entry Example',

    // Create the application itself
    _init: function() {
        this.application = new Gtk.Application({
            application_id: 'org.example.jsentry',
            flags: Gio.ApplicationFlags.FLAGS_NONE
        });

    // Connect 'activate' and 'startup' signals to the callback functions
    this.application.connect('activate', Lang.bind(this, this._onActivate));
    this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents windows when active
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
            title: "What is your name?"});

        // Create the text entry box
        this.entry = new Gtk.Entry ();
        this._window.add(this.entry);

        // Connect the text entry box to a function that responds to what you type in
        this.entry.connect("activate", Lang.bind (this, this._hello));

        // Show the window and all child widgets
        this._window.show_all();
    },



    _hello: function() {

        // Create a popup dialog to greet the person who types in their name
        this._greeter = new Gtk.MessageDialog ({
            transient_for: this._window,
            modal: true,
            text: "Hello, " + this.entry.get_text() + "!",
            message_type: Gtk.MessageType.OTHER,
            buttons: Gtk.ButtonsType.OK,
        });

        // Show the popup dialog
        this._greeter.show();

        // Bind the OK button to the function that closes the popup
        this._greeter.connect ("response", Lang.bind(this, this._okClicked));
    },

    _okClicked: function () {
        this._greeter.destroy();
    }

});

// Run the application
let app = new EntryExample ();
app.application.run (ARGV);
