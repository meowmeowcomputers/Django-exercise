from django.template.response import TemplateResponse
from django import forms
from django import http
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic



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

def poll(request):
    return TemplateResponse(request, 'poll.html', {})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
#
# def index (request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('index.html')
#     context = {
#             'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'
