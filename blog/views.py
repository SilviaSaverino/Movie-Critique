from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from .models import Post, MovieGenre, Director, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        reviews = post.reviews.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "reviews": reviews,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        reviews = post.reviews.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "reviews": reviews,
                "commented": True,
                "liked": liked,
                
                "comment_form": CommentForm()
            },
        )

class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def edit_review(request, review_id):
    review = get_object_or_404(Comment, id=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.warning(request, "Your edited review is awaiting approval")
            return redirect('post_detail', review.post.slug)
    else:
        form = CommentForm(instance=review)
    context = {'form': form, 'review': review, 'post': review.post}
    return render(request, 'edit_review.html', context)            



#----------------------------------------TO BE CHECKED WITH MENTOR


def MovieGenre_list(request):
    genres = MovieGenre.objects.all()
    return render(request,
                  'moviegenre_list.html',
                  {
                      'genres': genres
                      },
                  )


def MovieGenre_detail(request):
    genre = get_object_or_404(MovieGenre)
    directors = Director.objects.filter(genre=genre)
    return render(request,
                  'moviegenre_detail.html',
                  {
                    'genre': genre,
                    'director': director
                },
            )