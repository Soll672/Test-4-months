from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from film.views import (
    main_view,
    film_list_view,
    film_detail_view,

    actor_list_view,
    actor_detail_view,
    review_create_view
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view),
    path("films/", film_list_view, name="films_list"),
    path("films/<int:film_id>/", film_detail_view, name="film_detail"),
    path("films/<int:film_id>/review/", review_create_view, name="review_create"),
    path("actors/", actor_list_view, name="actors_list"),
    path("actors/<int:actor_id>/", actor_detail_view, name="actor_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)