from django.shortcuts import render, redirect
from django.contrib import messages as django_messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Project
from .forms import ContactForm


def index(request):
    projects = Project.objects.filter(is_active=True)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            # Notify admin
            send_mail(
                subject=f"Portfolio Contact: {contact_msg.subject}",
                message=f"From: {contact_msg.name} <{contact_msg.email}>\n\n{contact_msg.message}",
                from_email=contact_msg.email,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
            django_messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('home')
        else:
            django_messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'index.html', {
        'projects': projects,
        'form': form,
    })
