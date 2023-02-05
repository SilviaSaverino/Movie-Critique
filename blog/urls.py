from . import views
from django.urls import path
from .views import delete_review, UserRequestCreate, UserRequestUpdate, UserRequestDelete

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    #----------------------------------------to be checked with mentor
    path('director-request/create/', UserRequestCreate, name='director_request_form'),
    
    path('your-request/', views.YourRequest.as_view(), name='your_request'),
    path('request/<int:request_id>/edit/', views.UserRequestUpdate, name='edit_request'),
   
    
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
    
    path('genres/', views.MovieGenre_list, name='moviegenre_list'),
    path('genre/<int:genres_id>/', views.MovieGenre_detail, name='director_detail'),
    
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),

]