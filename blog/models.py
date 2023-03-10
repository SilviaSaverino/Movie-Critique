from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Main Table model post
    """
    title = models.CharField(max_length=400, unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Table model for Reviews
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"


class MovieGenre(models.Model):
    """
    Table model to represent movie genre
    """
    genre_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    age_rating = models.CharField(max_length=3, null=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.genre_name


class Director(models.Model):
    """
    Table model to represent movie directors
    """
    genre = models.ManyToManyField(
        MovieGenre, blank=True, related_name="director")
    director_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    bio = models.TextField()

    def __str__(self):
        return self.director_name


class UserRequest(models.Model):
    """
    Table model to represent a user request for a new director
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    director_name = models.CharField(max_length=50)
    genre = models.ManyToManyField(MovieGenre, blank=True)
    request = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.director_name
