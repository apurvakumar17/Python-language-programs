let socket = null;

function connectWebSocket() {
  socket = new WebSocket("ws://localhost:6969");

  socket.onopen = () => console.log("WebSocket connected!");

  socket.onmessage = (event) => {
    if (event.data === "toggle") {
      chrome.tabs.query({}, (tabs) => {
        const spotifyTab = tabs.find(tab => tab.url && tab.url.includes("open.spotify.com"));
        if (spotifyTab) {
          chrome.scripting.executeScript({
            target: { tabId: spotifyTab.id },
            func: () => {
              const btn = document.querySelector('[data-testid="control-button-playpause"]');
              if (btn) btn.click();
            }
          });
        }
      });
    }
  };

  socket.onclose = () => {
    console.warn("WebSocket disconnected. Retrying in 5s...");
    setTimeout(connectWebSocket, 5000);
  };

  socket.onerror = (e) => {
    console.error("WebSocket error:", e);
    socket.close();
  };
}

// keep-alive with chrome.alarms
chrome.runtime.onInstalled.addListener(() => {
  chrome.alarms.create("keepAlive", { periodInMinutes: 0.2 }); // every 12 sec
});

chrome.alarms.onAlarm.addListener(alarm => {
  if (alarm.name === "keepAlive") {
    console.log("Keep-alive ping");
  }
});

connectWebSocket();
