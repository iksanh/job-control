from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#data
posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]

def home(request):
    # return HttpResponse('<h1>Hello</h1>')
    context = {
        'posts' : posts,
        'title' : 'List Job'
    }
    return render(request, "jobs/home.html", context)


def about(request):
    return render(request, "jobs/about.html")