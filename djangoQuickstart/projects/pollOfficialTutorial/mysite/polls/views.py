from django.http import HttpResponse, Http404, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Question, Choice
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model= Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        exclude questions that haven't been published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#this is the same as below. do not use a generic template. this was an action that does not 
#have it's own particular template. 

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=[question.id]))


"""NON GENERIC VIEWS

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }

    return HttpResponse(render(request, 'polls/index.html', context))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    #question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(render(request, 'polls/detail.html', {'question': question}))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#this particular view handles a http POST
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=[question.id]))
"""
