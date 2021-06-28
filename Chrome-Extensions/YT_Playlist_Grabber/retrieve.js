
// Grabs all elements with ID video-title which should hold the link to the videos
// var links = $(".ytd-playlist-video-list-renderer").get();
var linkElements = document.querySelectorAll("ytd-playlist-video-renderer.ytd-playlist-video-list-renderer");
var links =[];


function printLinks(element, index) {
    console.log(element.links[0]);
} 

chrome.runtime.onMessage.addListener(   // This is to recieve messages from the extension
    function(request, sender, sendResponse) {
        console.log(sender.tab ?
                    "[YT-P] From a content script:" + sender.tab.url :
                    "[YT-P] From the extension to retrieve.js");

        if (request.message == "getLinks") {
            console.log("Length of elements: " + linkElements.length);
            console.log(linkElements);
            lenOfLinks = linkElements.length;
            for (i = 0; i < lenOfLinks; i++) {
                var anchor = linkElements[i].querySelector("#video-title");
                links[i] = "https://www.youtube.com/" + anchor.getAttribute("href").substring(1, 20);
            }
            // sendResponse({linkArray: links});
            chrome.runtime.sendMessage({ linkArray: links });
        }
    }
);
