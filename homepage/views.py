from django.template.response import TemplateResponse

def homepage (request):
    context = {
    'page_title': 'home page',
    'numbers': [1, 2, 3, 4]
    }
    return TemplateResponse(request, 'homepage.html', {})

def about (request):

    return TemplateResponse(request, 'about.html', {})
