const config = {
      apiKey: "AIzaSyAkwuO9GxcgxBrTJDrLF7SE4lUZNnewSn0",
      authDomain: "bastion-66cb2.firebaseapp.com",
      databaseURL: "https://bastion-66cb2.firebaseio.com",
      projectId: "bastion-66cb2",
      storageBucket: "bastion-66cb2.appspot.com",
      messagingSenderId: "1071327721533"
    };
firebase.initializeApp(config);
const database = firebase.database();

var oldURL = "";
var oldTime = new Date();

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  if (changeInfo.status === "complete") {
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
        console.log(tabs)
        var url = tabs[0].url;
        chrome.extension.getBackgroundPage().console.log("Old URL: " + oldURL);
        chrome.extension.getBackgroundPage().console.log("Current URL: " + url);
        oldURL = url;

        var urlData = new URL(url);
        var fixedString = urlData.hostname.replace(/\./g, "\\");
        console.log(fixedString);

        database.ref('hosts/' + fixedString).once('value').then(function(snapshot) {
          var data = snapshot.val();
          console.log(data)
          if (data === null) {
            data = {
              hits: {},
              totalHits: 0
            }
          }

          data.totalHits += 1;
          data.hits[(new Date()).getTime().toString()] = {
            path: urlData.pathname,
            timespent: (new Date() - oldTime),
          }

          database.ref('hosts/' + fixedString).set(data);
          oldTime = new Date();
        });
    });
  }
});