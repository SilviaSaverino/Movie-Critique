from django.contrib import admin
from .models import Post, Comment, User, Movie, Reviews
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



# BELOW TO BE DONE check this links for the django admin panel
# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
# DO NOT FORGET TO MIGRATE WHATEVER YOU ADD HERE -> python3 manage.py migrate

# @admin.register(User)
# class registerUser:

# @admin.register(Movie)
# class registerMovie:
    
# @admin.register(Reviews)
# class registerReviews:
    
