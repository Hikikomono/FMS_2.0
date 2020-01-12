--Softwareprojekt "Find my Stuff" or better "Find my Sh*t" --
--Authoren: Enko Roberto, Felber Christoph
--CSDC FH Campus Wien
--Projekt für Software Engineering

Unsere SRS Documente, HLD, Diaries etc findet man in unserem Google drive (Link auf Moodle.)

--MOSCOW:
Muss-Kriterien
Erstellen neuer Bookmarks in der Browserapp:
Der user kann über die Browserapp neue Bookmarks erstellen.
Der user muss einem Bookmark einen Titel vergeben.


Ein Tag erlaubt keine Leerzeichen.
Ein Tag wird zur Filterung von Bookmarks verwendet.
Die Suchfunktion der App zeigt Bookmarks die den Tag-Filterkriterien entsprechen an.

Ein Titel ist ein Zusammenschluss aus Zeichen, Leerzeichen sind hier erlaubt.
Eine URL ist entweder eine gewöhnliche Web-URL oder ein Pfad zu einer Ressource im lokalen Filesystem.
Eine URL hat keine maximale Zeichenanzahl.

In der Browserapp :
	save-Button: speichert das aktuelle Bookmark
	und schließt Browserapp


Die Browserapp lässt sich über einen Button direkt im Browser öffnen.


Die Windowsapp hat ein Suchfeld.
Das Suchfeld wird verwendet um Tags in der Liste der gespeicherten Bookmarks zu suchen.
	Durch Klick auf die URL wird man zu der jeweiligen Ressource weitergeleitet.

Wenn in der Windows App mehr Bookmark Einträge vorhanden sind als im User Interface darstellbar, können die weiteren mittels einer Scrollbar angezeigt werden.
In der Windows app gibt es die Möglichkeit neue Bookmarks zu erstellen.
	Dazu steht ein Button zur Verfügung.
Wenn ein neues Bookmark im Windows erstellt wird öffnet sich eine Eingabe in der URL, Titel, Tag, Kommentar hinzugefügt werden können.

Soll-Kriterien
Erstellen neuer Bookmarks in der Browserapp:
Tags werden durch Beistriche oder Leerzeichen abgeschlossen und voneinander getrennt.
Der user kann optional einen Kommentar zu einem Bookmark vergeben.
Die Browserapp fügt automatisch die aktuelle URL in das URL-Feld.
Der user kann die URL in der Browserapp bearbeiten.
Die Windowsapp hat seitlich ein Fenster in dem alle vergebenen Tags angezeigt werden.
Durch klick auf einen dieser Tags werden die gespeicherten Bookmarks danach gefiltert und angezeigt.
Ein Bookmark in der Windowsapp zeigt Titel und Tag an.
	Bei Klick auf Bookmark in Windowsapp wird der Kommentar sowie die URL angezeigt.
Durch rechtsklick auf das Bookmark in der Windowsapp öffnet sich ein Kontextmenü zur weiteren Bearbeitung (löschen, bearbeiten)


Bei der suche nach Bookmarks werden zuerst alle Tag-Treffer und danach die Titel-Treffer aufgelistet.
Ein Kommentar zu einem Bookmark besteht aus maximal 500 Zeichen.

Kann-Kriterien
Der user hat die Möglichkeit in der Browserapp über einen Button in die Windowsapp zu wechseln.
Das Browserapp Userinterface befindet sich nach dem öffnen im rechten oberen Rand des Browserfensters.
Das Browserapp Userinterface liegt intransparent über der Website als Overlay.
Das Browserapp Userinterface lässt sich nicht verschieben.
Das Browserapp Userinterface lässt sich nicht vom User skalieren.
Das seitliche Tag Fenster lässt sich über einen Button ausblenden.
Bei Start der Windowsapp werden Bookmarks zeitlich absteigend (nach Hinzufügedatu aufgelistet.





--Idee:
Bookmarkmanager für Online URLs sowie Filesystem URLs.
Ein Bookmark besteht aus tags (nach denen gefiltert werden kann),
aus einem Titel, URL und einem Kommentar.--

--Bestandteile:
Python Standalone Software
Chrome Extension
SQLite Datenbank--

--How To use:
open chrome browser (only possible here or other chromium-based browsers).
Go to menu->More Tools->Extensions.
Put on dev-mode (top right).
click "load unpacked" and load the folder "BrowserPlugin" from the project dir
Plugin can be opened on the small "F" Icon.

The Plugin can be used on any site to save a bookmark. When clicking on "F"
it automatically reads in the URL of the site as well as a title suggestion.
You now can choose your own tags (its important to seperate them with ','),
or change the title / URL. If you wish you can add a comment too.
Keep in mind that whitespaces in tags will be ignored.
when you finished press the "save" button.

When you finished saving several Bookmarks, and want to get them into the
main Python Software you need to press the "Sync" button in the plugin.
This will create and download a CSV file which inhabits all your bookmarks.
When the Python programm is started (works in windows & linux), the CSV file
will be parsed to actual Bookmark objects, and are added to the database.
Be careful - the CSV file will be deleted to keep sure that there is only 
one file in the Download folder.
WINDOWS USER: 
maybe you are asked where to put the csv file when clicking the sync button.
Please dont change the name and save it in your Downloads folder.

The Python Standalone:
(Run the file TestMain.py)
on the left side you can see all the tags that are deployed to your bookmarks.
you can click on them to put them into the search bar.
To search for a tag, you need to press the magnifying-glass icon.
if there is no tag in the search bar, it will reset your bookmark content.
The + button lets you add your own Bookmark (cool gimmick,
 if you copy paste a URL from web into it, it will crawl for a title)
- here you could also put in filesystem URLs!!!!
The Sync button lets you sync in a CSV file from the Downloads folder - 
this comes in handy when having the program running and using the 
Browserplugin in parallel.

The Bookmarks themselves have clickable Links to get to your saved bookmark,
and a "x" on top right to remove it. This will remove your Bookmark also from
the Database.
--
