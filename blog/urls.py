from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing-page"),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail"),
    path("read-later", views.ReadLater.as_view(), name="read-later"),
]
