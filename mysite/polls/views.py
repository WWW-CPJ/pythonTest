
# - 视图函数（Views）：视图是处理请求并返回响应的函数。每个视图函数接受一个请求对象 HttpRequest，并返回一个响应对象 HttpResponse。
from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # '''Return the last five published questions.'''
        # return Question.objects.order_by("-pub_date")[:5]

        # part5
        # return the last five published questions (not including those set to be published in tht future)
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]    
    # filter() 方法用于根据指定条件筛选数据。
    # pub_date：是 Question 模型中的一个字段，通常表示问题的发布时间。
    # __lte 是 Django ORM 中的查找操作符，表示“小于或等于”。
    # timezone.now() 返回当前的时间，表示只选取发布日期小于或等于当前时间的 Question 对象。
    #     order_by() 用来对查询结果进行排序。
    # "-pub_date" 表示按 pub_date 字段进行降序排序（- 符号表示降序，默认是升序）。
    # 也就是说，最新的（发布时间最晚的）问题会排在最前面。

    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """"
        Excludes any questions thst aren't published yet.
        """
        return Question.objects.filter(pub_date_lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



def index(request):
    # return HttpResponse("Hellp world. you are at the polls index.")
    # 返回http 响应，将数据作为响应返回客户端
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    # 加载模板、填充上下文并返回 HttpResponse带有渲染模板结果的对象是一种非常常见的习惯用法
    # Django 提供了一种快捷方式。以下是index()重写的完整视图：
    return render(request, "polls/index.html", context)
    # 视图的三要素 return render (request, template, context)


# 添加视图
# 通过在 polls/urls 中添加path 调用视图
def detail (request, question_id):
    # return HttpResponse("You are looking at question %s." % question_id)
    # 字符串格式化表达式。 %s 是一个占位符。将被 question_id 代替

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")    #Http404这里的新概念：如果不存在具有请求的 ID 的问题，视图将引发异常。
    # return render(request, "polls/detail.html", {"question": question})


    # 为什么我们要使用辅助函数，get_object_or_404() 而不是 ObjectDoesNotExist在更高级别自动捕获异常，或者让模型 APIHttp404引发 ObjectDoesNotExist？
    # 因为这样会将模型层与视图层耦合。Django 的首要设计目标之一就是保持松散耦合。django.shortcuts模块中引入了一些受控耦合。
    # 快捷方式，使用 get引发异常
    # 该get_object_or_404()函数将 Django 模型作为其第一个参数，并将任意数量的关键字参数传递给get()模型管理器的函数。Http404如果对象不存在，则会引发异常。
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    # response = "You are looking at thr results of question %s"
    # return HttpResponse(response % question_id)

    # part4 
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    # return HttpResponse("You are voting on the question %s." % question_id)

    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        #处理成功后总是返回一个HttpResponseRedirect
        #与POST数据。这可以防止数据被发布两次
        #用户点击后退按钮。
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


# Create your views here.
