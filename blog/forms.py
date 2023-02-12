from .models import Comment, UserRequest
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UserRequestForm(forms.ModelForm):

    class Meta:
        model = UserRequest
        fields = ['director_name', 'genre', 'request']

    def save(self, commit=True, user=None):
        """
        Override default save and link user to the author
        of the request.
        """
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()
        return instance
