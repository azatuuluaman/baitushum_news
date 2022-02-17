from django.shortcuts import render
from .models import News, Category


def news_list(request, pk):
    posts = News.objects.filter(category=pk)
    return render(request, 'news/news_list.html', {'posts': posts })


def cover(request):
    a = News.objects.all()
    category = Category.objects.all()
    return render(request, 'news/news_list.html', {'posts': a, 'category_list': category})
