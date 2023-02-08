# Generated by Django 4.1.6 on 2023-02-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_news_options_alter_news_avtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='shop_sizes',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large')], default='M', max_length=2),
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=1, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название статьи'),
        ),
    ]