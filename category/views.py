from django.shortcuts import render
from .models import Category

def category_list(request):
    posts = Category.objects.all()
    return render(request, 'category/category_list.html', {'posts': posts})


#view, или представление, — это то место, где мы разместим «логику» работы нашего приложения.
# Оно запросит информацию из модели, которую мы создали ранее, и передаст её в шаблон.

#render() Объединяет заданный шаблон с заданным контекстным словарем и возвращает объект HttpResponse с этим визуализированным кодом.