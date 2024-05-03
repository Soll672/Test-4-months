from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="films/")
    genres = models.ManyToManyField(Genre, related_name="films")
    actors = models.ManyToManyField(Actor, related_name="films")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.film.title} - {self.rating}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"