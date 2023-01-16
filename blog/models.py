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
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"


class User(models.Model):
    """
    Table model to represent the site user
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()


class Movie(models.Model):
    """
    Table model represent the site movie
    """
    title = models.CharField(max_length=70)
    release_date = models.DateField()
    genre = models.CharField(max_length=70)
    director = models.CharField(max_length=70)


class Reviews(models.Model):
    """
    Table model represent the site reviews
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_content = models.TextField(max_length=255)
