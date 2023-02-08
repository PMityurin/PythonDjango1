from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата и время', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE) #

    views = models.IntegerField('Просмотры', default=1)
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X Large')
    # )
    # shop_sizes = models.CharField(max_length=2, choices=sizes, default="M")

    # on_delete=models.CASCADE удалить
    # все статьи
    # если пользователь будет удален
    def __str__(self):
        return  self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk':self.pk})


