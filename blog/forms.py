from .models import Comment, UserRequest  # MovieGenre
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UserRequestForm(forms.ModelForm):

    class Meta:
        model = UserRequest
        fields = ['director_name', 'genre', 'request']
