from django.urls import path

from . import views
app_name = 'comment'

urlpatterns = [
    path('comment/<int:pk>',views.CommentDetail.as_view(),name='comment'),



]