from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            recipients = ['pavel.yansapov@gmail.com']

            send_mail(subject, message, sender, recipients)
            return render(request, 'feedback_form/thanks.html')

    else:
        form = ContactForm()

    return render(request, 'feedback_form/contact.html', {'form': form})