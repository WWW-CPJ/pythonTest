from django.shortcuts import render
from .models import Chapters as SearchItem
from django.core.paginator import Paginator

def search_view(request):
    query = request.GET.get('q')  # 从请求的 GET 参数中获取搜索关键字，如果没有则为空字符串
    if query:
        # 如果有关键字，在 SearchAppSearchitem 模型中搜索章节包含该关键字的记录
        results = SearchItem.objects.filter(chapter__icontains=query)
    else:
        results = SearchItem.objects.all()  # 如果没有关键字，获取所有记录
    results = results.order_by('id')  # 按 ID 倒序排列

    paginator = Paginator(results, 10)  # 创建 Paginator 实例，每页显示10条记录
    page_number = request.GET.get('page')  # 获取请求的页码，如果没有则默认为第 1 页
    page_obj = paginator.get_page(page_number)  # 获取指定页码的页对象

    return render(request, 'search_app/search.html', {'page_obj': page_obj, 'query': query})  # 渲染模板，传递页对象和关键字到模板中进行渲染