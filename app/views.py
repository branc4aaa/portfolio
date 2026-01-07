from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'home1.html')

def proj_view(request):
    proj = Project.objects.all()
    return render(request, 'projects.html', {'projects': proj})

def about_view(request, pid:int):
    pro = get_object_or_404(Project, id=pid)
    con = {'id':pro.id, 'name':pro.name, 'tag':pro.tag, 'urltag':pro.urltag,'info':pro.info}

    return render(request, 'about.html', con)

def more_view(request):
    return render(request, 'more.html')

