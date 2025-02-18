import sys
import os
import django

# 集成 Scrapy 时，需要在 Scrapy 项目中导入 Django 模型，需要设置 Django 环境
# 但是在 Scrapy 项目中导入 Django 模型会报错，所以需要设置 Django 环境
# 但还是报错了
def setup_django_env():

    # 获取 Django 项目的绝对路径
    django_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../search_project'))

    # 将 Django项目路径添加到 Python 模块搜索路径中，把 django_project_path 添加到 sys.path 列表的末尾。
    sys.path.append(django_project_path)

    # # 会把 django_project_path 插入到 sys.path 列表的索引为 0 的位置，也就是列表开头。
    # sys.path.insert(0, django_project_path)

    # 设置 Django 的配置文件路径
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_project.settings')

    # 初始化 Django 环境
    django.setup()





