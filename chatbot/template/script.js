document.getElementById('chatToggle').addEventListener('click', function() {
  var chatbox = document.getElementById('chatbox');
  chatbox.style.display = chatbox.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('chatClose').addEventListener('click', function() {
  document.getElementById('chatbox').style.display = 'none';
});

document.getElementById('userInput').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    var userInput = document.getElementById('userInput');
    var message = userInput.value.trim();
    if (message) {
      addMessage('user', message);
      userInput.value = '';
      sendAutoReply(message);
    }
  }
});

function addMessage(sender, message) {
  var chatMessages = document.getElementById('chatMessages');
  var messageElement = document.createElement('div');
  messageElement.classList.add('message');
  messageElement.innerHTML = '<strong>' + sender + ':</strong> ' + message;
  chatMessages.appendChild(messageElement);
}

function sendAutoReply(message) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/get_bot_response', true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          var response = JSON.parse(xhr.responseText).response;
          addMessage('user', message);
          addMessage('Chatbot', response);
      }
  };
  xhr.send('msg=' + encodeURIComponent(message));
}
