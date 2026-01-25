from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home1.html')

def proj_view(request):
    proj = Project.objects.all()
    return render(request, 'projects.html', {'projects': proj})

def about_view(request, pid: int):
    pro = get_object_or_404(Project, id=pid)

    images = pro.images.all()  
    context = {
        'project': pro,
        'images': images,
    }

    return render(request, 'about.html', context)
def more_view(request):
    return render(request, 'more.html')

def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    
        return render(request, 'contact.html', {'form': form})

    form = ContactForm()

    return render(request, 'contact.html', {'form': form})

