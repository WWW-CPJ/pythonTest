import datetime

from django.db import models
from django.utils import timezone

#  模型就是数据库中的一张表
#  QuestionAdmin 作为一个管理类，定义了如何在后台展示和操作该表的数据。


# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# 这段代码定义了两个 Django 模型：Question 和 Choice。这两个模型可以用于表示一个简单的投票应用中的问题和选项
# class Question (models.Model):                                # 表示Question 是一个模型，继承自 models.Model.
#                                                               # Django 的模型类都需要继承自 models.Model，以便它们能够使用 Django 的 ORM 功能。
#     question_text = models.CharField(max_length=200)          # question_text 是一个字符字段，用于存储问题的文本。
#                                                               # max_length=200 指定该字段的最大字符数为 200
#     pub_date = models.DateTimeField("data published")         # pub_date 是一个日期时间字段，用于存储问题的发布时间。
#                                                               # "data published" 是该字段的可读标签，通常用于 Django 管理界面或表单中。

# class Choice (models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)        
#     # question 是一个外键字段，指向 Question 模型。这表示每个选择（Choice）都与一个问题（Question）关联。
#     # on_delete=models.CASCADE 表示如果相关的 Question 被删除，则与之相关的所有 Choice 也会被删除。这是为了维护数据的完整性。
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     # votes 是一个整数字段，表示该选项的投票数。
#     # default=0 表示新创建的选项的默认投票数为 0。


# 这段代码实现了一个简单的投票系统的数据模型：
# Question 模型用于表示问题，包括问题文本和发布日期。
# Choice 模型表示与每个问题相关的选项，包括选项文本和投票数。
# 通过外键关联，Django 可以轻松地在这两个模型之间建立关系，方便进行查询和数据操作。

