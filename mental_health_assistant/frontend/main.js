
async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.innerText = userInput;
    chatBox.appendChild(userMessage);

    const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: userInput })
    });

    const data = await response.json();
    const botMessage = document.createElement("div");
    botMessage.className = "bot-message";
    botMessage.innerText = data.response;
    chatBox.appendChild(botMessage);

    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}
