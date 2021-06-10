document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('clickIt');
    checkPageButton.addEventListener('click', function() {
  
      // chrome.tabs.getSelected(null, function(tab) {
      //   alert("Hello..! It's my first chrome extension.");
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
          console.log(response.farewell);
        });
      });
      
    }, false);

  }, false);

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    
    request.playlistLinks.forEach(myFunction);
  }
);



function myFunction(item, index) {
  console.log(item.attr('href'));
} 