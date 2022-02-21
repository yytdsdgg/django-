# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserLoginForm,UserRegisterForm
from django.views.generic import FormView,View,DetailView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import BlogUser

# Create your views here.
#用户登录
class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'usermanage/login.html'
    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST,request=self.request)
        if form.is_valid():
            login(self.request,form.get_user())
            return  super(LoginView,self).form_valid(form)
        else: return HttpResponse("账号或密码错误。请重新输入")

    def get_success_url(self):
        return reverse('blog:article_list')

#用户登出(RedirectView重定向)
class LogoutView(View):
    
    def get(self, request,*args, **kwargs):
        logout(request)
        return redirect('usermanage:login')



#注册用户视图
class RegisterUser(FormView):
    form_class = UserRegisterForm
    template_name = 'usermanage/register.html'
    def form_valid(self, form):
        if form.is_valid():
            # new_user = user_register_form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            login(self.request, new_user)
            url = reverse('usermanage:user_detail',kwargs={'pk':new_user.id})
            return HttpResponseRedirect(url)
        else:
            return HttpResponse("输入信息无效")

#用户删除
class UserDelete(DeleteView):
    template_name = 'usermanage/delete.html'
    model = BlogUser

    def post(self,request,*args, **kwargs):
        user = get_user_model().objects.get(id=self.get_object().id)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('usermanage:login')
        else: return HttpResponse('无删除权限')




#用户详情视图
class UserDetail(DetailView):
    model = BlogUser
    template_name = 'usermanage/user_detail.html'


#用户信息修改
class UserDetailUpdate(UpdateView):
    model = BlogUser
    template_name = 'usermanage/user_detail_update.html'
    fields = ['avatar','nikename','email','profile']

    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=self.get_object().id)
        if request.user!=user:
            return HttpResponse("你没有修改的权限")
        return super(UserDetailUpdate, self).post(request,*args,**kwargs)

    def form_valid(self, form,*args,**kwargs):
        return super().form_valid(form,*args,**kwargs)

    def get_success_url(self):
        return reverse('usermanage:user_detail',kwargs={'pk':self.object.pk})

