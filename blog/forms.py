from .models import Comment, UserRequest  # MovieGenre
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
        
# class MovieGenreForm(forms.ModelForm):
#     class Meta:
#         model = MovieGenre
#         fields = ['genre_name']
        
#     def clean_genre_name(self):
#         genre_name = self.cleaned_data.get('genre_name')
#         if MovieGenre.objects.filter(genre_name=genre_name).exists():
#             raise forms.ValidationError("A genre with this name already exists.")
#         return genre_name

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['director_name', 'genre', 'request']