from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone

from .models import News, Category


def news_list(request, pk):
    ''' Выдает новости по выбранной категории'''
    posts = News.objects.filter(category=pk)
    return render(request, 'news/news_list.html', {'posts': posts})


def cover(request):
    ''' Выдает все новости '''
    a = News.objects.order_by('-published_date')
    category = Category.objects.all()
    return render(request, 'news/news_list.html', {'posts': a, 'category_list': category})


def test(request):
    ''' Поисковик '''
    q = request.GET['search_text']
    n = News.objects.filter(
        Q(text__icontains=q) | Q(subtitle__icontains=q) | Q(title__icontains=q))
    return render(request, 'news/news_list.html', {'posts': n})

def bootstrap_views(request):
    '''Bootstrap карусель'''
    a = News.objects.order_by('-published_date')
    category = Category.objects.all()
    return render(request, 'news/bootstrap.html', {'posts': a, 'category_list': category})

