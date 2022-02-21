from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, Http404,HttpResponse


# Create your views here.
def index(request):
    return render(request,'blog/index.html')
#文章列表视图
class AirticleListview(ListView):
    model = Article
    template_name='blog/airticle_listview.html'



#文章视图
class AirticleView(DetailView):
    model = Article
    template_name = 'blog/artdetail.html'

    def get(self, request, *args, **kwargs):
        response = super(AirticleView,self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response

    # def post(self,request,*args,**kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()
    #     self.object = self.get_object()
    #     form = self.get
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self,form):
    #     return super(AirticleView, self).form_valid()



#文章增删改
class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Article
    fields = ['title','body']
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user != get_user_model().objects.get(id=1):
            return HttpResponse("无权限管理")
        return super(ArticleCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("blog:article_list")



class ArticleDelete(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:article_list')

    def delete(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=self.get_object().author.id)
        if request.user != user:
            return HttpResponse("无权限管理")
        return super(ArticleDelete, self).delete(request,*args,**kwargs)



class ArticleUpdate(LoginRequiredMixin,UpdateView):
    model = Article
    template_name = 'blog/update.html'
    fields = ['title','body']

    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=self.get_object().author.id)
        if request.user!=user:
            return HttpResponse("无权限管理")
        return super(ArticleUpdate, self).post(request,*args,**kwargs)

    def get_success_url(self):
        return reverse("blog:article_detail",kwargs={'pk':self.object.pk})




