from django.db import models
from django.utils import timezone

from blog.models import Article

# Create your models here.
# #评论table
class Comment(models.Model):
    nikename = models.CharField('昵称',max_length=50,blank=True,default='匿名')
    email = models.EmailField('邮箱',unique=True,blank=True)
    context = models.TextField('评论内容',blank=False)
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    arti = models.ForeignKey(Article,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        ordering = ('-created_time',)

    def __str__(self):
        return '{}:{}'.format(self.nikename,self.context[:20])





