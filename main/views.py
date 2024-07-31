from django.shortcuts import render
def home(request):
    data={
        'title':"Coder's Code",
    }
    return render(request,'index.html',data)