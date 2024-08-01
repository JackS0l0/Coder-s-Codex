from typing import Any
from django.shortcuts import render
from .models import Topadvertising,Trend,Article,Categories
from django.views.generic import DetailView
class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        pass