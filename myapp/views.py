from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Task

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    #return HttpResponse("hello world")
    tasks = Task.objects.all()
    return render(request,'myapp/index.html',{'tasks':tasks})
