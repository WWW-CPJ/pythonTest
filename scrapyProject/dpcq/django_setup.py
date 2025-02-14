import sys
import os
import django

def setup_django_env():

    # 获取 Django 项目的绝对路径
    django_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../search_project'))

    # 将 Django项目路径添加到 Python 模块搜索路径中
    sys.path.append(0, django_project_path)

    # 设置 Django 的配置文件路径
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_project.settings')

    # 初始化 Django 环境
    django.setup()





