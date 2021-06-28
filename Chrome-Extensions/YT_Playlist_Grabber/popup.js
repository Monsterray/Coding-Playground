console.log('<----- Extension script started running ----->');


function writeLinkstoPopup(item, index) { 
  console.log("[INFO] Trying to write an array");

  let divNode = document.getElementById('container');
  let node = document.createTextNode (item);

  divNode.appendChild(node);
  divNode.appendChild(document.createElement("br"));
} 

function grabDataFunc(sentEvent) {  // Function for when the grabData button is clicked
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs){    // Find the active tab
    chrome.tabs.sendMessage(tabs[0].id, {message: "getLinks"});             // Send a message to found tab
  }, false);
}

document.addEventListener('DOMContentLoaded', function() {    // Event triggered when the page is fully loaded
  var checkPageButton = document.getElementById('clickIt');   // Find button with ID 'clickIt'
  checkPageButton.addEventListener('click', function() {      // Add a listener to wait for the button to be clicked
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) { // Find the active tab
      chrome.tabs.sendMessage(                                // Send a message to found tab
        tabs[0].id, {message: "getLinks"});
    });
  }, false);

  var getDataBtn = document.getElementById('grabData');       // Find button with ID 'clickIt'
  checkPageButton.addEventListener('clickGrabData', grabDataFunc);  // Add a listener to wait for the button to be clicked
}, false);

chrome.runtime.onMessage.addListener(                         // Event trigered when a message is sent from the background or content script
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    
    request.linkArray.forEach(writeLinkstoPopup);
  }
);


// window.addEventListener('DOMContentLoaded', () => {  // This would be for making comunication with the background page
//     let bg = chrome.extension.getBackgroundPage();

//     chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
//         let currentTabId = tabs[0].id;
//         let currentYTPlay = bg.YTPlay[currentTabId];

//         if (!currentYTPlay) {
//           return;
//         }

//         currentYTPlay.forEach(writeLinkstoPopup);
        
//     });
// });

