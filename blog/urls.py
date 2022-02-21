from django.urls import path
from .views import AirticleListview,AirticleView,ArticleCreate,ArticleDelete,ArticleUpdate

from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('article_list/',AirticleListview.as_view(),name = 'article_list'),
    path('article_list/<int:pk>',AirticleView.as_view(),name = 'article_detail'),
    path('article_list/add',ArticleCreate.as_view(),name='article_add'),
    path('article_list/<int:pk>/update',ArticleUpdate.as_view(),name='article_update'),
    path('article_list/<int:pk>/delete',ArticleDelete.as_view(),name='article_delete'),
]