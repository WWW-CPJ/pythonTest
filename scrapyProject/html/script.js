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
        // 调用 AI 模型获取回复
        const response = await getAIResponse(message);
        const aiMessage = document.createElement('div');
        aiMessage.textContent = `AI: ${response}`;
        chatMessages.appendChild(aiMessage);
    } catch (error) {
        console.error('Error getting AI response:', error);
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Error getting AI response. Please try again later.';
        chatMessages.appendChild(errorMessage);
    }
}

// 调用 AI 模型获取回复
async function getAIResponse(message) {
    const apiUrl = 'wss://spark-api.xf-yun.com/v1.1/chat';
    // 替换为你的讯飞星火 API 密钥
    const apiKey = '6729815a2d91fc53c8e70f192c6c1600'; 
    // 替换为你的讯飞星火 App ID
    const appId = 'dccdfdd5'; 

    const requestBody = {
        app_id: appId,
        messages: [
            {
                role: "user",
                content: message
            }
        ],
        temperature: 0.5,
        max_tokens: 2048,
        model: "generalv3.5",
        stream: false // 根据需求设置是否流式返回
    };

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 可能需要根据文档调整
                'Authorization': `Bearer ${apiKey}` 
            },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            // 打印详细的错误信息
            const errorText = await response.text();
            console.error('API request failed:', response.status, errorText);
            throw new Error('API request failed');
        }

        const data = await response.json();
        console.log('API response data:', data); // 打印 API 响应数据

        // 根据实际响应结构调整
        if (data.choices && data.choices.length > 0 && data.choices[0].message) {
            return data.choices[0].message.content;
        } else {
            throw new Error('Invalid response structure');
        }
    } catch (error) {
        console.error('Error in getAIResponse:', error);
        throw error;
    }
}