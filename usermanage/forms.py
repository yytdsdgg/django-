from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,get_user_model
from django.forms import widgets
from django.core.exceptions import ValidationError


# 登录表单，继承了 forms.Form 类
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})


class UserRegisterForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget = widgets.TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
        self.fields['email'].widget = widgets.EmailInput(
            attrs={'placeholder': "email", "class": "form-control"})
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={'placeholder': "repeat password", "class": "form-control"})

    class Meta:
        model=get_user_model()
        fields = ['username','email','password1','password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("改邮箱已经存在")
        return email

    # def clean_password(self):
    #     data = self.cleaned_data
    #     if data.get('password1') ==data.get('password2'):
    #         return data.get('password1')
    #     else:
    #         return forms.ValidationError('两次密码不一样')


