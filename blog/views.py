from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Promise',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 23, 2024'
    },
    {

        'author': 'Rocky',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 24, 2024'


    }

]


def home(requests):
    context = {
        'posts': posts
    }
    return render(requests, 'blog/home.html', context)

def about(requests):
    return render(requests, 'blog/about.html', {'title': 'About'}) 