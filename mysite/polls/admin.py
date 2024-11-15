from django.contrib import admin
from .models import Question


# 继承自 admin.ModelAdmin。ModelAdmin 是 Django 提供的一个类，用于定制模型在管理后台的表现。
# 通过继承 ModelAdmin，你可以控制模型在后台的显示和交互方式。
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
# 将你创建的 QuestionAdmin 类与 Question 模型注册到 Django 管理后台。
# 这样，Django 管理后台就会使用你定制的 QuestionAdmin 类来管理 Question 实例。