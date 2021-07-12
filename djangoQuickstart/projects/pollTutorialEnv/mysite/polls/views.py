from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

#view to see details on specific question
def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question #{question_id}')

#view to see vote results for a particular question
def results(request, question_id):
    return HttpResponse(f'You\'re looking at the results for question #{question_id}')

#view to make a vote on a particular question
def vote (request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')
