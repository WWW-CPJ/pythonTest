// 切换聊天机器人对话框的显示和隐藏
function toggleChatbot() {
    const chatbotContainer = document.getElementById('chatbot-container');
    chatbotContainer.classList.toggle('hidden');
}

// 发送消息
async function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value;
    if (message.trim() === '') return;

    // 显示用户消息
    const chatMessages = document.getElementById('chatbot-messages');
    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${message}`;
    chatMessages.appendChild(userMessage);

    // 清空输入框
    userInput.value = '';

    try {
        // 调用后端 API 获取回复
        const response = await fetch('/chatbot-api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'message': message
            })
        });

        const data = await response.json();
        if (data.response) {
            const aiMessage = document.createElement('div');
            aiMessage.textContent = `AI: ${data.response}`;
            chatMessages.appendChild(aiMessage);
        } else {
            const errorMessage = document.createElement('div');
            errorMessage.textContent = `Error: ${data.error}`;
            chatMessages.appendChild(errorMessage);
        }
    } catch (error) {
        console.error('Error getting AI response:', error);
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Error getting AI response. Please try again later.';
        chatMessages.appendChild(errorMessage);
    }
}