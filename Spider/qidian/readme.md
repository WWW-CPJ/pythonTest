scrapy + django + eltsicsearch
参考文献：
https://blog.csdn.net/qq_35394891/article/details/82952774
https://www.cnblogs.com/jinxiao-pu/p/6706319.html

scrapy:
pip install scrapy
pip install requests
pip install beautifulsoup4

scrapy  搭建框架，requests 获取网页，beautifulsoup 解析提取字段

scrapy startproject qidian
cd qidian
scrapy genspider qidian qidian.com
编写 spider 
scrapy crawl qidian


Django:
https://www.djangoproject.com/start/


pip install django           # python -m django --version     查看django 版本

创建项目 
django-admin startproject mysite
# django-admin startproject mysite djangotutorial         # 这种命令，创建文件夹为djangotutorial ,文件夹下面包含 mysite 项目



