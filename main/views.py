from django.shortcuts import render
from articles.models import Topadvertising,Trend,Categories,Article
def home(request):
    data={
        'title':"Coder's Code",
        'topadvertising': Topadvertising.objects.all()[0:1],
        'trend': Trend.objects.all().order_by('-date'),
        'categories': Categories.objects.all().order_by('name'),
        'article_first_cover': Article.objects.all().order_by('-date')[0:1],
        'article_second_cover': Article.objects.all().order_by('-date')[1:2],
        'article_third_cover': Article.objects.all().order_by('-date')[2:3],
        'article_fourth_cover': Article.objects.all().order_by('-date')[3:4],
        'article_mob_cover': Article.objects.all().order_by('-date')[0:4],
    }
    return render(request,'index.html',data)