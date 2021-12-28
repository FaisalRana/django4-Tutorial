from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# what happens when the user goes to a url 

def index(request): 
  meetups = [
    { 'title': 'A First Meetup'},
    { 'title': 'A second Meetup'}
  ]
  return render(request, 'meetups/index.html', {
      'meetups': meetups,
      'show_meetups': False,
    })