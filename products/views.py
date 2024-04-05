from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from.models import Item

# Create your views here.
def index(request):
    products= Item.objects.all()
    return render(request,'index.html',{'products':products})
def about(request):
    return HttpResponse("<h1>About</h1>")
