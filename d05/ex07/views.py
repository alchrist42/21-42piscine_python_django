from django import db
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UpdateForm
from .models import Movies


def populate(request):
    data = [
        [1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"],
        [2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"],
        [3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"],
        [4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"],
        [
            5,
            "The Empire Strikes Back",
            "Irvin Kershner",
            "Gary Kurtz, Rick McCallum",
            "1980-05-17",
        ],
        [
            6,
            "Return of the Jedi",
            "Richard Marquand",
            "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "1983-05-25",
        ],
        [
            7,
            "The Force Awakens",
            "J. J. Abrams",
            "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "2015-12-11",
        ],
    ]

    results = []
    for line in data:
        try:
            episode_nb, title, director, producer, release_date = line
            Movies.objects.create(
                episode_nb=episode_nb,
                title=title,
                director=director,
                producer=producer,
                release_date=release_date,
            )
            results.append("OK")
        except db.Error as e:
            results.append(e)

    return HttpResponse("<br/>".join(str(i) for i in results))


def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            raise Movies.DoesNotExist
        return render(request, 'ex07/display.html', {"movies": movies})
    except Movies.DoesNotExist as e:
        return HttpResponse("No data available movies")


def update(request):
    movies = Movies.objects.all()
    titles = [(movie.title, movie.title) for movie in movies]
    msg = ""
    if request.method == 'POST':
        form = UpdateForm(titles, request.POST)
        if form.is_valid():
            movie_to_upd = form.cleaned_data['title']
            new_crawl = form.cleaned_data['opening_crawl']
            try:
                movie = Movies.objects.get(title=movie_to_upd)
                movie.opening_crawl = new_crawl
                movie.save()
                msg = f"{movie_to_upd} updated"
                movies = Movies.objects.all()
            except Exception as e:
                msg = e
        else:    
            msg = "invalid form"

    return render(request, 'ex07/update.html', {'form': UpdateForm(titles), "movies": movies, "msg": msg})
