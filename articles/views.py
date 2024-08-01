from typing import Any
from django.shortcuts import render
from .models import Topadvertising,Trend,Article,Categories
from django.views.generic import DetailView
class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        data=super(ArticleDetail,self).get_context_data(**kwargs)
        data['title']=Article.objects.get(pk=self.kwargs['pk'])
        data['categories']=Categories.objects.all().order_by('name')
        data['topadvertising']=Topadvertising.objects.all()[0:1]
        return data