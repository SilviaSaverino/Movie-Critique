from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
#----------------------------------------to be checked with mentor
    path("genre/", views.genre_list, name="genre_list"),
    path("genre/<int:genre_id>/", views.genre_detail, name="genre_detail"),
]