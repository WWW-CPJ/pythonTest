from django.urls import path

from . import views

#  patterns 模式，模型
# 在这里 添加path后 调用视图
# 视图写完之后，要在这里先映射才能在浏览器中进行访问
# 即 路由 routing 部分
# 路由管理：Django 使用 URL 路由系统，将请求的 URL 映射到相应的视图函数。
app_name = "polls"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # 更改后
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]