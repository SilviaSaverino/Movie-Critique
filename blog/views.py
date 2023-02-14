from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
# this is the code added
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
# --------
from django.shortcuts import redirect
from .models import Post, MovieGenre, Director, Comment, UserRequest
from .forms import CommentForm, UserRequestForm   # MovieGenreForm


class PostList(generic.ListView):
    """
    Displays a list of approved blog posts on the home page,
    in descending order.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(View):
    """
    Displays a specific blog post when requested.
    It also allows the user to like the post and leave reviews.
    """
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
    """
     Allows the user to like or unlike a specific post
     by handling the post request.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def edit_review(request, review_id):
    """
    Allows the user to edit a review that they have
    previously submitted, by handling the post request.
    """
    review = get_object_or_404(Comment, id=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.warning(
                request, "Your edited review is ready")
            return redirect('post_detail', review.post.slug)
    else:
        form = CommentForm(instance=review)
    context = {'form': form, 'review': review, 'post': review.post}
    return render(request, 'edit_review.html', context)


def delete_review(request, review_id):
    """
    Allows the user to delete a review that they have
    previously submitted
    """
    review = get_object_or_404(Comment, id=review_id)
    review.delete()
    messages.warning(request, "Deleting your review")
    return redirect('post_detail', slug=review.post.slug)


# ----------------------------------------MovieGenre


def MovieGenre_list(request):
    """
    Show a list of all movie genres
    """
    genres = MovieGenre.objects.all()
    return render(request,
                  'moviegenre_list.html',
                  {
                      'genres': genres
                      },
                  )


def MovieGenre_detail(request, genres_id):
    """
    Show details of a specific movie genre and
    movie directors
    """
    genre = get_object_or_404(MovieGenre, id=genres_id)
    directors = Director.objects.filter(genre=genre)
    return render(request,
                  'director_detail.html',
                  {
                    'genre': genre,
                    'directors': directors
                  },
                  )

# ----------------------------------------UserRequest


def UserRequestCreate(request):
    """
    Handle creation of a director request
    """
    if request.method == 'POST':
        form = UserRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.approved = False
            form.save(user=request.user)
            messages.success(
                request, 'Director request submitted successfully')
            return redirect('your_requests')
    else:
        form = UserRequestForm()
    return render(request, 'director_request_form.html', {'form': form})


def UserRequestUpdate(request, request_id):
    """
    Handle editing of a director request
    """
    user_request = get_object_or_404(UserRequest, id=request_id)
    if str(user_request.author) != str(request.user.username):
        return HttpResponse("You cannot edit this request", status=403)
    if request.method == 'POST':
        form = UserRequestForm(request.POST, instance=user_request)
        if form.is_valid():
            form.save()
            messages.warning(
                request, "Your edited request is ready")
            return redirect('your_requests')
    else:
        form = UserRequestForm(instance=user_request)
    return render(request, 'director_request_form.html', {'form': form})


def UserRequestDelete(request, request_id):
    """
    Handle deletion of a user request
    """
    user_request = get_object_or_404(UserRequest, id=request_id)
    user_request.delete()
    messages.warning(request, "Deleting your request")
    return redirect('your_requests')


class YourRequest(generic.ListView):
    model = UserRequest
    template_name = 'your_requests.html'
    context_object_name = 'user_requests'
