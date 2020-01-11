--Softwareprojekt "Find my Stuff" or better "Find my Sh*t" --
--Authoren: Enko Roberto, Felber Christoph
--CSDC FH Campus Wien
--Projekt für Software Engineering

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
The + button lets you add your own Bookmark - for example a filesystem URL.
The Sync button lets you sync in a CSV file from the Downloads folder - 
this comes in handy when having the program running and using the 
Browserplugin in parallel.

The Bookmarks themselves have clickable Links to get to your saved bookmark,
and a "x" on top right to remove it. This will remove your Bookmark also from
the Database.
--
