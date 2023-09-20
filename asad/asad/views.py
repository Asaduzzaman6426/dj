from django.shortcuts import render, HttpResponse

def home (request):
    return render(request,'index.html')
def test (request):
    return render(request,'test.html')