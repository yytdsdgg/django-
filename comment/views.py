from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#评论视图
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin

from blog.models import Article
from .forms import CommentForm
from .models import Comment
from django.urls import reverse

#加新评论
class CommentDetail(FormMixin,DetailView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/artdetail.html'
    context_object_name = 'comment'
    def get_success_url(self):
        return reverse('blog:article_detail',kwargs={'pk':self.object.arti.pk})
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form(request.POST)
        if form.is_vaild():

            return self.form_valid(form)
        else:
            return HttpResponse("不合法")

        
    def form_valid(self, form):
        comment = form.save(commit=False)
        arti_id = self.kwargs['arti_id']
        article = Article.objects.get(pk=arti_id)
        comment.article = article
        if self.request.user.is_authenticated():
            comment.nikename = self.request.user.username
            comment.email = self.request.user.email
        comment.save()
        return super(CommentDetail, self).form_valid(form)


