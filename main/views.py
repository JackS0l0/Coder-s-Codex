from django.shortcuts import render
from articles.models import Topadvertising,Trend,Categories,Article
def home(request):
    data={
        'title':"Coder's Code",
        'topadvertising': Topadvertising.objects.all()[0:1],
        'trend': Trend.objects.all().order_by('-date'),
        'categories': Categories.objects.all().order_by('name'),
        'article_first_cover': Article.objects.all().order_by('-date')[0:1],
    }
    return render(request,'index.html',data)