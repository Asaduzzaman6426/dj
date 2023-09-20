from django.shortcuts import render,HttpResponse

# Create your views here.
def my(request):
    return render(request,"my.html")