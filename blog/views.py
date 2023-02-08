from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def home(request):
    # news = [
    #     {
    #         'title': 'Наша первая статья',
    #         'text': 'Полный текст статьи',
    #         'date': '1 Января 2100 года',
    #         'avtor': 'Джон'
    #     },
    #     {
    #         'title': 'Наша вторая статья',
    #         'text': 'Полный текст статьи',
    #         'date': '21 Января 2100 года',
    #     }
    # ]
    # data = {
    #     'news': News.objects.all(),
    #     'title': 'Главная страница'
    # }
    # return render(request, 'blog/home.html', data)

class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f'Статьи от пользователя {self.kwargs.get("username")}'
        return ctx

class ShowView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowView, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    # context_object_name = 'post'
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateNewsView(CreateView, LoginRequiredMixin):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

class UpdateNewsView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = News
    template_name = 'blog/create_news.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def get_context_data(self, **kwards):
        ctx = super(DeleteNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Удаление статьи'
        ctx['btn_text'] = 'Удалить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

def contacti(request):
    return render(request, 'blog/contacti.html', {'title':'Страница контакты!'})
# Create your views here.
