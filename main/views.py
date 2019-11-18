from django.shortcuts import render

# We will map urls pattern to this view function in 'urls.py' module(file)


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
