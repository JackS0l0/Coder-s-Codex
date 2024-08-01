from django.shortcuts import render
from articles.models import Topadvertising,Trend
def home(request):
    data={
        'title':"Coder's Code",
        'topadvertising': Topadvertising.objects.all()[0:1],
        'trend': Trend.objects.all().order_by('-date'),
    }
    return render(request,'index.html',data)