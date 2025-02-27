
from django.shortcuts import render
from .models import Chapters as SearchItem
from django.core.paginator import Paginator
import subprocess
import os
from django.conf import settings
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_scrapy_crawl():
    scrapy_project_dir = os.path.abspath(os.path.join(settings.BASE_DIR, '../dpcq'))
    try:
        # 切换到 scrapy 项目目录
        os.chdir(scrapy_project_dir)
        # 运行 scrapy 爬虫命令，并捕获标准输出和标准错误输出
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

def search_view(request):
    query = request.GET.get('q')  # 从请求的 GET 参数中获取搜索关键字，如果没有则为空字符串
    if query:
        # 运行爬虫
        run_scrapy_crawl()
        # 如果有关键字，在 SearchAppSearchitem 模型中搜索章节包含该关键字的记录
        results = SearchItem.objects.filter(chapter__icontains=query)
    else:
        results = SearchItem.objects.all()  # 如果没有关键字，获取所有记录
    results = results.order_by('id')  # 按 ID 倒序排列

    paginator = Paginator(results, 10)  # 创建 Paginator 实例，每页显示10条记录
    page_number = request.GET.get('page')  # 获取请求的页码，如果没有则默认为第 1 页
    page_obj = paginator.get_page(page_number)  # 获取指定页码的页对象

    return render(request, 'search_app/search.html', {'page_obj': page_obj, 'query': query})  # 渲染模板，传递页对象和关键字到模板中进行渲染





# from django.shortcuts import render
# from .models import Chapters as SearchItem
# from django.core.paginator import Paginator

# def search_view(request):
#     query = request.GET.get('q')  # 从请求的 GET 参数中获取搜索关键字，如果没有则为空字符串
#     if query:
#         # 如果有关键字，在 SearchAppSearchitem 模型中搜索章节包含该关键字的记录
#         results = SearchItem.objects.filter(chapter__icontains=query)
#     else:
#         results = SearchItem.objects.all()  # 如果没有关键字，获取所有记录
#     results = results.order_by('id')  # 按 ID 倒序排列

#     paginator = Paginator(results, 10)  # 创建 Paginator 实例，每页显示10条记录
#     page_number = request.GET.get('page')  # 获取请求的页码，如果没有则默认为第 1 页
#     page_obj = paginator.get_page(page_number)  # 获取指定页码的页对象

#     return render(request, 'search_app/search.html', {'page_obj': page_obj, 'query': query})  # 渲染模板，传递页对象和关键字到模板中进行渲染