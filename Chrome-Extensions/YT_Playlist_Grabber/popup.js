

function writeLinkstoPopup(item, index) {
  var textnode = document.createTextNode(item);
  document.appendChild(textnode);
} 

document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('clickIt'); // Find button with ID 'clickIt'
    checkPageButton.addEventListener('click', function() {    // Add a listener to wait for the button to be clicked
      
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) { // Find the active tab
        chrome.tabs.sendMessage(                              // Send a message to found tab
          tabs[0].id, {message: "getLinks"},

          function(response) {
            console.log(response.farewell);
          }
        );
      });

    }, false);

  }, false);

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    
    request.linkArray.forEach(writeLinkstoPopup);
  }
);

