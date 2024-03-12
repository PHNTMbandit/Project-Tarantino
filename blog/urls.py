from . import views
from django.urls import path

urlpatterns = [
    path("", views.landing_page, name="landing-page"),  # type: ignore
    path("posts", views.posts, name="posts"),  # type: ignore
    path("posts/<slug:slug>", views.post_detail, name="post-detail"),  # type: ignore
]
