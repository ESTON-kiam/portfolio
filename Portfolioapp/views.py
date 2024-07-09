from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from Portfolioapp.forms import ContactForm
from Portfolioapp.models import ContactMessage


# Create your views here.
def home(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'service-details.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')


def contact_form_email(request):
    return render(request, 'contact_form_email.html')


def contact_form_success(request):
    return render(request, 'contact_form_success.html')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            admin_email = 'engestonbrandonkiama@gmail.com'
            subject_email = 'New Contact Form Submission: ' + subject
            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
            html_message = render_to_string('contact_form_email.html', context)
            plain_message = strip_tags(html_message)

            send_mail(
                subject_email,
                plain_message,
                settings.EMAIL_HOST_USER,
                [admin_email],
                html_message=html_message,
            )

            return render(request, 'contact_form_success.html')

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
