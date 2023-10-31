from django.shortcuts import render

def home(request):
    posts = []  # Replace with the actual list of posts you want to display
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 