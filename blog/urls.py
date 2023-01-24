from . import views
from django.urls import path
from .views import delete_review

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    #----------------------------------------to be checked with mentor
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
    path('genres/', views.MovieGenre_list, name='moviegenre_list'),
    path('genre/', views.MovieGenre_detail, name='moviegenre_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),

]