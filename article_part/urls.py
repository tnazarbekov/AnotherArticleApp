from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_home, name='article_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.OurTemplateView.as_view(), name='article_detail'),
    path('<int:pk>/update', views.OurUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete', views.OurDelete.as_view(), name='article_delete'),
]
