import os
import django

def setup_django_env():
    # 设置 Django 的配置文件路径
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_project.settings')
    django.setup()