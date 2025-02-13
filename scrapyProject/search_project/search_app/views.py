from django.shortcuts import render

from .models import SearchItem
from django.core.paginator import Paginator
# Create your views here.

def search_view(request):
    query = request.GET.get('q')        # 从请求的 GET 参数中获取搜索关键字，如果没有则为空字符串
    if query:
        # 如果有关键字，在 Article 模型中搜索标题或内容包含该关键字的文章
        results = SearchItem.objects.filter(title__icontains=query) | SearchItem.objects.filter(connect__icontains=query)
    else:
        results = SearchItem.objects.all()   # 如果没有关键字，获取所有文章
    results = results.order_by('-created')    # 按创建时间倒序排列

    if results:
        paginator = paginator(results, 10)          # 创建 Paginator 实例  分页器，每页显示10篇文章
        page_number = request.GET.get('page')               # 获取请求的页码，如果没有则默认为第 1 页
        page_obj = paginator.get_page(page_number)           # 获取指定页码的页对象
    else:
        # 如果 results 为空，创建一个空的分页器
        paginator = Paginator([], 10)
        page_obj = paginator.get_page(1)
        
    return render(request, 'search_app/search.html', {'page_obj': page_obj, 'query': query})   # 渲染模板，传递页对象和关键字到模板中进行渲染

    