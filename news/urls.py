from django.urls import path
from . import views

urlpatterns = [
    path('news_list/<pk>', views.news_list, name='news_list'),
    path('', views.cover, name='news_list'),

    path('search', views.test, name='test_url_name'),

    path('bootstrap', views.bootstrap_views, name="bootstrap")
]

