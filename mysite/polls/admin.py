from django.contrib import admin
from .models import Question, Choice




# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 继承自 admin.ModelAdmin。ModelAdmin 是 Django 提供的一个类，用于定制模型在管理后台的表现。
# 通过继承 ModelAdmin，你可以控制模型在后台的显示和交互方式。
class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]

    # part 7
    # fieldsets = [
    #     ("Question title", {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"]}),
    # ]
    # # 列表中有两个元组，元组中有两个元素。一个是string，一个是字典

    fieldsets = [
        ("question title", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    # polls 列表页展示的
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # 右侧添加的过滤器
    list_filter = ["pub_date"]
    # 顶部添加搜索框
    search_fields = ["question_text"]



# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
# 将你创建的 QuestionAdmin 类与 Question 模型注册到 Django 管理后台。
# 这样，Django 管理后台就会使用你定制的 QuestionAdmin 类来管理 Question 实例。