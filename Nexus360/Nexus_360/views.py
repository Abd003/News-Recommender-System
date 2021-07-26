# Nexus360
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import News_Post
from .forms import addArticleForm,updateArticleForm
from django.template import loader
from django.urls import reverse_lazy



# Create your views here.

class HomeView(ListView):
    model=News_Post
    template_name='home.html'
    ordering=['-date']

class News_detail_view(DetailView):
    model=News_Post
    template_name='news_detail.html'

class Add_article_view(CreateView):
    model=News_Post
    template_name='add_article.html'
    form_class=addArticleForm
    #fields='__all__'

class Update_article_view(UpdateView):
    model=News_Post
    form_class=updateArticleForm
    template_name='updateArticle.html'
    #fields=['title','News_content']
class Delete_article_view(DeleteView):
    model=News_Post
    template_name='delete_article.html'
    success_url=reverse_lazy('home')
