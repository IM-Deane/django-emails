from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render

from templated_mail.mail import BaseEmailMessage


def email(request):
    """
    Basic email
    """
    try:
        send_mail(
            'subject',
            'DELICIOUS!',
            'rengoku@demonslayer.com',
            ['test@example.com']
        )
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Rengoku'})


def admin_email(request):
    """
    Demonstrates how to email all Django admins.
    """
    try:
        mail_admins(
            'subject',
            'Yooo',
            html_message='hey friend' # will show html if mail client allows, else send text based
        )
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Tanjiro'})


def attachment(request):
    """
    Send an email with an attachment.
    """
    try:
       message = EmailMessage('subject', 'message', 'from@mandalore.sw', [
        'rengoku@demonslayer.com'
       ])
       message.attach_file('playground/static/images/canderous-ordo.webp')
       message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mandalore'})


def template(request):
    """
    Send a templated email.
    """
    try:
       message = BaseEmailMessage(
           template_name='emails/hello.html',
           context={
               'name': 'Ricky Bobby'
           }
        )
       message.send(
           ['test@example.cool'] # recipients
        )
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Ricky Bobby'})