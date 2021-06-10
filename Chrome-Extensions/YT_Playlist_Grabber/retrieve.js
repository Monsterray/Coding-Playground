
// Grabs all elements with ID video-title which should hold the link to the videos
// var links = $(".ytd-playlist-video-list-renderer").get();
var linkElements = document.querySelectorAll("ytd-playlist-video-renderer.ytd-playlist-video-list-renderer");


function printLinks(element, index) {
    console.log(element.links[0]);
} 

chrome.runtime.onMessage.addListener(   // This is to recieve messages from the extension
    function(request, sender, sendResponse) {
        console.log(sender.tab ?
                    "[YT-P] From a content script:" + sender.tab.url :
                    "[YT-P] From the extension in retrieve.js");
        if (request.greeting == "hello")
            sendResponse({farewell: "goodbye"});

        console.log("Length of elements: " + linkElements.length);
        console.log(linkElements);
        lenOfLinks = linkElements.length;
        for (i = 0; i < lenOfLinks; i++) {
            var anchor = linkElements[i].querySelector("#video-title");
            console.log("https://www.youtube.com/" + anchor.getAttribute("href"));
        }
    }
);

chrome.runtime.sendMessage({playlistLinks: linkElements}, 
    function(response) {
        console.log("[YT-P] There is a response at retrieve.js");
    }
);


// /watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&index=1
// /watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&index=1