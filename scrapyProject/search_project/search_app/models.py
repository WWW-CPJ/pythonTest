from django.db import models

# Create your models here.
class SearchItem(models.Model):
    # title = models.CharField(max_length=200)    #文章标题。最大长度200
    # content = models.TextField()            #文章内容
    # created = models.DateTimeField(auto_now_add=True)   #创建时间
    chapter = models.CharField(max_length=200)    #小说章节名称
    link = models.CharField(max_length=500, default='https://www.doupocangqiong.org/doupocangqiong/')


    def __str__(self):
        # 返回文章标题，用于在后台 管理界面显示或者其他地方显示文章标题
        return self.chapter
    