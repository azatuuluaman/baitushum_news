from django.db import models
from category.models import Category


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок', null=True)
    text = models.TextField(verbose_name='Текст')
    category = models.ForeignKey( Category , on_delete=models.CASCADE , null=True)
    # category = models.ManyToManyField( Category )
    image = models.ImageField(upload_to='images/', null=True)
    published_date = models.TimeField(blank=True, null=True)

