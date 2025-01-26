document.getElementById('send-btn').addEventListener('click', function() {
  var userInput = document.getElementById('user-input').value;
  if (userInput.trim() === "") {
      return;
  }

  // Append user's question to the chat
  var chatBox = document.getElementById('chat-box');
  var userMessage = document.createElement('div');
  userMessage.classList.add('user-message');
  userMessage.textContent = "You: " + userInput;
  chatBox.appendChild(userMessage);

  // Clear the input field
  document.getElementById('user-input').value = '';

  // Send the question to the server
  fetch('/ask', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          question: userInput,
      }),
  })
  .then(response => response.json())
  .then(data => {
      // Display the answer from the chatbot
      var botMessage = document.createElement('div');
      botMessage.classList.add('bot-message');
      botMessage.textContent = "Bot: " + data.answer;
      chatBox.appendChild(botMessage);

      // Scroll to the bottom of the chat
      chatBox.scrollTop = chatBox.scrollHeight;
  })
  .catch(error => console.error('Error:', error));
});
