from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("links/", views.links, name="links"),
    path("article/<int:id>/", views.article, name="article"),
    path("booklist/<int:id>/", views.booklist, name="booklist"),
    path("comment/", views.comment, name="comment"),
]