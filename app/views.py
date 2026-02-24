from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMessage  
from django.conf import settings
from .models import Project
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'app/home1.html')

def proj_view(request):
    proj = Project.objects.all()
    return render(request, 'app/projects.html', {'projects': proj})

def about_view(request, pid: int):
    pro = get_object_or_404(Project, id=pid)

    images = pro.images.all()  
    context = {
        'project': pro,
        'images': images,
    }

    return render(request, 'app/about.html', context)

def more_view(request):
    return render(request, 'app/more.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Contacto portfolio: {name}"
            body = f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}"

            mail = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECEIVER_EMAIL],
                reply_to=[email],
            )
            mail.send()

            messages.success(request, "contacto enviado correctamente.")
            form = ContactForm() 

    else:
        form = ContactForm()

    return render(request, "app/contact.html", {"form": form})