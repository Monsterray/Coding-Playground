
window.YTPlay = {};

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    window.YTPlay[sender.tab.id] = message.linkArray || null;
});