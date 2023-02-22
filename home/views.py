from django.shortcuts import render, redirect


def index(request):
    """ A view to return the index page """

    if request.user.is_authenticated:
        return redirect('feed/')
    else:
        return render(request, 'home/index.html')
