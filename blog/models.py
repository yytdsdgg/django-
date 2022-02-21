from django.db import models
from django.contrib.auth.forms import get_user_model
from django.utils import timezone
from django.urls import reverse
from mdeditor.fields import MDTextField

# Create your models here.
#文章类
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = MDTextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, editable=False)
    class Meta:
        ordering = ('create_time',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("blog:article_list")

    def increase_views(self):
        self.views += 1
        self.save(update_fields=["views"])


# #登录table
# class Account(models.Model):
#     pass








