from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    #----------------------------------------to be checked with mentor
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('moviegenres/', views.MovieGenre_list, name='moviegenre_list'),
    path('moviegenre/', views.MovieGenre_detail, name='moviegenre_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),

]