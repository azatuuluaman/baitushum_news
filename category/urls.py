from django.urls import path
from . import views

urlpatterns = [
    path('category_list/', views.category_list, name='category_list'),
]

# если url адрес будет пустой , то направляем в view.py к функции category_list,
# часть name='category_list' — это имя URL, которое будет использовано, чтобы идентифицировать его