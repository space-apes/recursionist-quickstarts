from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    context = {}
    context['show_meetups'] = True
    context['meetups'] = [
        {
            'title': 'A first Meetup',
            'location': 'New York',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A second Meetup',
            'location': 'Paris', 
            'slug': 'a-second-meetup'
        },
    ]
    return render(request, 'meetups/index.html', context)

def meetup_detail(request, meetup_slug):
    selected_meetup = {
        'title': 'A first Meetup',
        'description': 'This is the first meeting!'
    }
    
    context = {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    }
    return render(request, 'meetups/meetup-details.html', context)
