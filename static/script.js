// Function to get the current time as HH:MM
function getCurrentTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

// Function to add a message to the chat box
function addMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    
    // Determine the sender class (user or bot)
    const senderClass = (sender === 'user') ? 'user' : 'bot';
    
    // Create the message HTML
    const messageHTML = `
        <div class="message ${senderClass}">
            ${message}
            <span class="timestamp">${getCurrentTime()}</span>
        </div>`;
        
    chatBox.innerHTML += messageHTML;
    
    // Auto-scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Main function to send a message
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (!message) return; // Don't send empty messages

    // 1. Add the user's message to the chat box
    addMessage('user', message);

    // 2. Clear the input field
    input.value = "";

    // 3. Send the message to the Flask backend
    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => {
        // 4. Add the bot's reply to the chat box
        addMessage('bot', data.reply);
    })
    .catch(() => {
        // 5. Add an error message if something goes wrong
        addMessage('bot', 'Sorry, something went wrong.');
    });
}