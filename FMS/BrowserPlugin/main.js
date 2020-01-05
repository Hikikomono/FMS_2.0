//Array for Bookmarks if already exists in chrome storage it should be reloaded
let bookmarkArray = new Array();
chrome.storage.sync.get(['array'],function(result){
    bookmarkArray = result.array;
});

//now the query to get the url of active tab into the input field
let field = document.getElementById("inputUrl");
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
    field.value = url;
});

//bind butons to variables
let saveBtn = document.getElementById("saveBtn");
let syncBtn = document.getElementById("syncSaves");



//savebutton function (inserting new Bookmarks to array)
saveBtn.addEventListener("click", addToArray);
//syncbutton function (getting a csv out of the array)
syncBtn.addEventListener("click",getCSV);


//for dev purpose only
let removeBtn = document.getElementById("remove");
removeBtn.addEventListener("click",removeData);
function removeData() {
    //removes all data from storage (achtung lokal ist es da bis restart logischerweise)
chrome.storage.sync.clear();
}

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
        alert("success!");
        console.log("added bookmarkArray to storage")
    });



    //window.alert("saved Bookmark");
}

function getCSV(){
    //function saves .csv file of the Bookmarks array on local HD for sync with standalone Python

    alert(bookmarkArray[3]);


    displayInfo("...bookmarks synced");
}