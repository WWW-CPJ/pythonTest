const spawn = require('cross-spawn');

// 使用 cross-spawn 运行 scrapy 命令
const scrapyProcess = spawn('scrapy', ['crawl', 'dpcqHome'], {stdio: 'inherit'});

// 监听 scrapy 爬虫进程退出
scrapyProcess.on('close', (code) => {
    if (code === 0 ) {
        console.log('Scrapy spider ran successfully');
    } else {
        console.log(`Scrapy spider failed with code ${code}`);
    }
});