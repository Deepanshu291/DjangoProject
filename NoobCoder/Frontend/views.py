from django.shortcuts import render

# Create your views here.
def index(req):
    list = [i for i in range(10)]
    return render(req,'index.html',{"list":list})