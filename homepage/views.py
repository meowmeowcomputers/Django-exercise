from django.template.response import TemplateResponse
from django import forms
from django import http
from django.core.mail import send_mail


class NameForm (forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

class EmailInput (forms.Form):
    user_email = forms.CharField(label='User Email')
    # user_name = forms.CharField(label='User Name')

def homepage (request):
    form = NameForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['your_name'])
            return http.HttpResponseRedirect('/thanks')
    context = {
        'form': form
        }
    return TemplateResponse(request, 'homepage.html', context)

def about (request):
    return TemplateResponse(request, 'about.html', {})

def index (request):
    return TemplateResponse(request, 'index.html', {})

def contact(request):
    form  = EmailInput(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            send_mail('Subject here',
            'Here is the message. Test 2',
            form.cleaned_data['user_email'],
            ['ryan@ryansimonleon.com'],
            fail_silently=False,)
            print(form.cleaned_data['user_email'])
            return http.HttpResponseRedirect('/contact')

    context = {
        'form': form
    }
    return TemplateResponse(request, 'contact.html', context)
