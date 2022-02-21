from django.urls import path
from . import views

app_name = 'usermanage'

urlpatterns = [
    # 用户登录
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/',views.RegisterUser.as_view(),name = 'register'),
    path('logout/<int:pk>',views.LogoutView.as_view(),name ='logout'),
    path('user_detail/<int:pk>',views.UserDetail.as_view(),name = 'user_detail'),
    path('user_detail/<int:pk>/update',views.UserDetailUpdate.as_view(),name = 'user_detail_update'),
    path('delete_user/<int:pk>',views.UserDelete.as_view(),name = 'user_delete')
]