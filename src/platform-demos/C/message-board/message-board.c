/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */

#include <config.h>
#include <gtk/gtk.h>
#include <webkit/webkit.h>


#include <glib/gi18n.h>

static const guchar CSS[] =
"body { margin: 0; padding: 0; }\n"
"div { "
" -webkit-border-radius: 2px;"
" background: -webkit-gradient(linear, 0% 100%, 0% 0%,"
" from(#f1f1f1), to(white));"
" border: solid 1px #c6c6c6;"
" -webkit-box-shadow: 0px 0px 2px #c6c6c6;"
" margin: 12px; padding: 6px;"
"}";

static void
entry_activate_cb (GtkEntry *entry, WebKitWebView *view)
{
	WebKitDOMDocument *document;
	WebKitDOMElement *body, *div;

	document = webkit_web_view_get_dom_document (view);
	body = webkit_dom_document_query_selector (document,
	                                           "body",
	                                           NULL);
	div = webkit_dom_document_create_element (document,
	                                          "div",
	                                          NULL);
	webkit_dom_node_set_text_content (WEBKIT_DOM_NODE (div),
	                                  gtk_entry_get_text (entry),
	                                  NULL);
	webkit_dom_node_append_child (WEBKIT_DOM_NODE (body),
	                              WEBKIT_DOM_NODE (div),
	                              NULL);
	gtk_entry_set_text (entry, "");
}

static GtkWidget*
create_window (void)
{
    GtkWidget *window, *box, *scroll, *view, *entry;
	gchar *tmp, *css;

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (window), 400, 400);
    gtk_window_set_title (GTK_WINDOW (window), "Message Board");
	g_signal_connect (window, "delete-event",
	                  G_CALLBACK (gtk_main_quit), NULL);

    box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 6);
    gtk_container_set_border_width (GTK_CONTAINER (box), 6);
    gtk_container_add (GTK_CONTAINER (window), box);

    entry = gtk_entry_new ();
    gtk_box_pack_start (GTK_BOX (box), entry, FALSE, FALSE, 0);

    scroll = gtk_scrolled_window_new (NULL, NULL);
	g_object_set (scroll, "shadow-type", GTK_SHADOW_IN, NULL);
    gtk_box_pack_start (GTK_BOX (box), scroll, TRUE, TRUE, 0);

    view = webkit_web_view_new ();
    gtk_container_add (GTK_CONTAINER (scroll), view);
    webkit_web_view_load_string (WEBKIT_WEB_VIEW (view),
	                             "<html><body></body></html>",
	                             "text/html",
	                             "UTF-8",
	                             NULL);

	tmp = g_base64_encode (CSS, strlen((gchar *) CSS));
	css = g_strconcat ("data:text/css;charset=utf-8;base64,",
	                   tmp, NULL);
	g_object_set (webkit_web_view_get_settings (WEBKIT_WEB_VIEW (view)),
	              "user-stylesheet-uri", css, NULL);
	g_free (css);
	g_free (tmp);

	g_signal_connect (entry, "activate",
	                  G_CALLBACK (entry_activate_cb), view);

	gtk_widget_show_all (GTK_WIDGET (box));
	return window;
}

int
main (int argc, char *argv[])
{
 	GtkWidget *window;


#ifdef ENABLE_NLS
	bindtextdomain (GETTEXT_PACKAGE, PACKAGE_LOCALE_DIR);
	bind_textdomain_codeset (GETTEXT_PACKAGE, "UTF-8");
	textdomain (GETTEXT_PACKAGE);
#endif

	gtk_init (&argc, &argv);

	window = create_window ();
	gtk_widget_show (window);

	gtk_main ();
	return 0;
}
