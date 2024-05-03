from django.db import models
from django.db.models import Q
from django.shortcuts import redirect, render

from film.forms import ReviewForm
from film.models import Film, Actor, Review


def main_view(request):
    return render(request, "main.html")


def film_list_view(request):
    query = request.GET.get('query', '').strip()

    if query:
        films = Film.objects.filter(
            Q(title__icontains=query) | Q(genres__name__icontains=query)
        ).distinct()  # Добавляем .distinct() для устранения дубликатов
    else:
        films = Film.objects.all()

    return render(request, "films/list.html", {"films": films})

def film_detail_view(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        return render(request, "errors/404.html")
    
    review_form = ReviewForm()
    context = {
        "film": film,
        "review_form": review_form
    }

    return render(request, "films/detail.html", context)


def actor_list_view(request):
    actors = Actor.objects.all().annotate(rating=models.Avg("films__rating")).order_by("-rating")

    return render(request, "actors/list.html", {"actors": actors})


def actor_detail_view(request, actor_id):
    try:
        actor = Actor.objects.get(id=actor_id)
    except Actor.DoesNotExist:
        return render(request, "errors/404.html")
    
    # Решение используя Python
    # actor_rating = sum([film.rating for film in actor.films.all()]) / len(actor_films) if actor_films else 0

    # Решение используя Django ORM
    actor_rating = actor.films.aggregate(models.Avg("rating"))["rating__avg"]
    context = {
        "actor": actor,
        "actor_rating": actor_rating
    }

    return render(request, "actors/detail.html", context)


def review_create_view(request, film_id):
    if request.method == "POST":
        try:
            film = Film.objects.get(id=film_id)
        except Film.DoesNotExist:
            return render(request, "errors/404.html")
        
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                Review.objects.create(
                    film=film,
                    text=form.cleaned_data["text"],
                    rating=form.cleaned_data["rating"]
                )
                return redirect("film_detail", film_id=film_id)
        else:
            form = ReviewForm()
        
        return render(request, "films/detail.html", {"film": film, "review_form": form})


