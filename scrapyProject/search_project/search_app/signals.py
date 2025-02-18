# myapp/signals.py
import os
import subprocess
from django.core.signals import request_started
from django.conf import settings
from django.dispatch import receiver
from apscheduler.schedulers.background import BackgroundScheduler
import logging

import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@receiver(request_started)
def start_scrapy_scheduler(sender, **kwargs):
    scheduler = BackgroundScheduler()

    def run_scrapy_crawl():
        scrapy_project_dir = os.path.abspath(os.path.join(settings.BASE_DIR, '../dpcq'))

        try:
            # 切换到 scrapy 项目目录
            os.chdir(scrapy_project_dir)
            # 运行 scrapy 爬虫命令，并捕获标准输出和标准错误输出
            # result = subprocess.run(['scrapy', 'crawl', 'chapters'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)
            result = subprocess.run(['scrapy', 'crawl', 'chapters'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True, encoding='utf-8')
            # 输出爬虫运行的日志
            logger.info("Scrapy spider output:\n%s", result.stdout)
            # 输出成功信息
            logger.info("scrapy spider run successfully")
        except subprocess.CalledProcessError as e:
            # 输出错误信息和错误日志
            logger.error("Scrapy crawl failed: %s\n%s", e, e.output)
        except Exception as e:
            logger.error("An error occurred: %s", e)

    # 添加定时任务，每隔十分钟运行一次
    scheduler.add_job(run_scrapy_crawl, 'interval', minutes=20)
    scheduler.start()

    # 立即运行一次爬虫
    run_scrapy_crawl()