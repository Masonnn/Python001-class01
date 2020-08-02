from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .models import Doubanmovies


def movies_info(request):
    allMovies = Doubanmovies.objects.all()
    conditions = {'film_stars_gt': 3}

    # allMovies = Movies.filter(**conditions)

    return render(request, 'result.html', locals())
