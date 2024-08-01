from django.shortcuts import render
from articles.models import Topadvertising,Trend,Categories,Article
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
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