from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Tag, Comment
from django.db.models import Q
from .forms import RegisterForm, CommentForm, PostForm




# -----------------------------
# REGISTRATION
# -----------------------------
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})

# -----------------------------
# PROFILE VIEW
# -----------------------------
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")

    return render(request, "blog/profile.html")



class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'  
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-published_date']

# Detail view (public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = self.object.comments.all()

        context["comment_form"] = CommentForm()

        comment_id = self.request.GET.get("edit")
        if comment_id:
            comment = Comment.objects.get(id=comment_id)
            context["comment_form"] = CommentForm(instance=comment)
            context["editing_comment"] = comment

        return context


# Create new post (only authenticated)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=True)
        return super().form_valid(form)

# Update post (only author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
    def form_valid(self, form):
        post = form.save(commit=True)
        return super().form_valid(form)

# Delete post (only author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user






@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.author = request.user
        new_comment.post = post
        new_comment.save()
        return redirect('post_detail', pk=post.id)

    return redirect('post_detail', pk=post.id)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return redirect('post_detail', pk=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)

    return redirect('post_detail', pk=comment.post.id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_id = comment.post.id
    comment.delete()
    return redirect('post_detail', pk=post_id)





def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)

    return render(request, "blog/tag_posts.html", {
        "tag": tag,
        "posts": posts
    })


def search_posts(request):
    q = request.GET.get('q', '').strip()
    posts = Post.objects.none()
    if q:
        posts = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(tags__name__icontains=q)
        ).distinct().order_by('-published_date')
    return render(request, 'blog/search_results.html', {'query': q, 'posts': posts})
