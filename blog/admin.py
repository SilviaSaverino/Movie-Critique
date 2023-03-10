from django.contrib import admin
from .models import Post, Comment, User, Director, MovieGenre, UserRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approved_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Director)
class DirectorAdmin(SummernoteModelAdmin):
    list_display = ('director_name', 'slug')
    search_fields = ['director_name', 'content']
    prepopulated_fields = {'slug': ('director_name',)}
    summernote_fields = ('content')


@admin.register(MovieGenre)
class MovieGenre(SummernoteModelAdmin):
    list_display = ('genre_name', 'slug')
    search_fields = ['genre_name', 'content']
    prepopulated_fields = {'slug': ('genre_name',)}
    summernote_fields = ('content')


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('director_name',)
    list_filter = ('approved',)
    search_fields = ['director_name']
    actions = ['approve_director_request']
