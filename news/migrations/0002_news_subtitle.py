# Generated by Django 4.0.2 on 2022-02-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='subtitle',
            field=models.CharField(max_length=50, null=True, verbose_name='Подзаголовок'),
        ),
    ]
