from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
#图片保存动态路径
def custom_path(instance,filename):
    username = instance.username
    return 'user_avatar/{}/{}'.format(username,filename)

#自定义用户模型
class BlogUser(AbstractUser):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='custom_user')
    nikename = models.CharField('昵称',max_length=50,blank = True)
    avatar = models.ImageField('头像',upload_to=custom_path,blank=True)
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    update_time=models.DateTimeField('修改时间',auto_now=True)
    profile = models.CharField('个人简介',max_length=240,blank=True)

    def get_absolute_url(self):
        return reverse('usermanage:user_detail',kwargs={'author_name':self.username})

    def __str__(self):
        return self.username

    # @receiver(post_save,sender=User)
    # def create_user(sender,instance,created,**kwargs):
    #     if created:
    #         BlogUser.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user(sender,instance,**kwargs):
    #     instance.custom_user.save()

    class Meta:
        ordering = ['-id']
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

