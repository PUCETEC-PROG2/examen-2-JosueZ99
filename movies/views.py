from django.template import loader
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index (request):
    movies = Movie.objects.order_by('title')
    template = loader.get_template('index.html')
    context = {'movies': movies}
    return HttpResponse(template.render(context, request))

def display_movie (request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    template = loader.get_template('display_movie.html')
    context = {'movie': movie}
    return HttpResponse(template.render(context, request))