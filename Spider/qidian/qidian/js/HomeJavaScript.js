function refreshHomePage() {
    const messageDiv = document.getElementById('refreshHomePageMessage');
    messageDiv.style.display = 'block';

    setTimeout(() => {
        window.location.reload();
    }, 1000);  // 1秒后刷新
}