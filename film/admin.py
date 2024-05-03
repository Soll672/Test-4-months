from django.contrib import admin

from film.models import Actor, Film, Genre, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
    search_fields = ("name",)
    list_filter = ("age",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "rating")
    search_fields = ("title",)
    list_filter = ("year", "rating")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("film", "rating", "created_at")
    search_fields = ("film",)
    list_filter = ("rating", "created_at")