//Array for Bookmarks
let bookmarkArray = new Array();

//now the query to get the url of active tab
let field = document.getElementById("inputUrl");
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
    field.value = url;
});

let saveBtn = document.getElementById("saveBtn");
let syncBtn = document.getElementById("syncSaves");

//savebutton function (inserting new Bookmarks to array)
saveBtn.addEventListener("click", addToArray);
//syncbutton function (getting a csv out of the array)
syncBtn.addEventListener("click",getCSV);

function displayInfo(message){
    //next function let a message appear for some seconds (together with css)
    document.getElementById("timeoutAlert").innerHTML = '<p>'+message+'</p>';
    document.getElementById("timeoutAlert").style.color = "#333333";

    setTimeout(function () {
        document.getElementById("timeoutAlert").innerHTML = '';
    }, 2000);
}

//TODO: check if its persistent now, make a get of storage with every start of the extension, then check if its really persisted
function addToArray() {
    //function adds inserted Data to an array that can be converted to .csv later
    let url = document.getElementById("inputUrl").value;
    let title = document.getElementById("inputTitle").value;
    let tag = document.getElementById("inputTag").value;
    let comment = document.getElementById("inputComment").value;

    bookmarkArray.push([url,title,tag,comment]);

    chrome.storage.sync.set({'array': bookmarkArray}, function () {
    //message that it worked
    });



    //window.alert("saved Bookmark");
}

function getCSV(){
    //function saves .csv file of the Bookmarks array on local HD for sync with standalone Python

    window.alert(bookmarkArray[3]);


    displayInfo("...bookmarks synced");
}