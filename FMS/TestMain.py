"""Just for Testing purposes"""

from FMS.Caretaker import Caretaker
from FMS.Bookmark import Bookmark
from FMS.DbController import DbController

test = DbController()
test.init_tables()

carer = Caretaker()
# bookmark1 = Bookmark(1, "lala", "url", "comment","picture", ["list"])


carer.add_bookmark(None, "My first entry", "www.sex.at", "my comment111", None, ["lulu", "gaga"])
carer.add_bookmark(None, "My second entry", "www.sex.lulu", "my comment222", None, ["pipi", "vagai"])

# carer.delete_bookmark(carer.bookmark_list[1])

# for elements in carer.bookmark_list:
#    print(elements.id)

print(carer.bookmark_list[-1].id)


