from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Contact
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, PostForm


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True).exclude(username=request.user)
    return render(request, 'blog/user/user_list.html', {'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'blog/user/user_detail.html', {'user': user})


# подписаться/отписаться на какого либо автора
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return redirect('blog:user_list')
        except User.DoesNotExist:
            return redirect('blog:user_list')
    return redirect('blog:user_list')


def post_list(request):
    posts = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_post = PostForm(request.POST)
            if form_post.is_valid():
                cd = form_post.cleaned_data
                new_post = form_post.save(commit=False)
                new_post.author = request.user              
                new_post.save()
                return redirect('blog:post_list')
        else:
            form_post = PostForm()
        posts = Post.objects.filter(author=request.user)       
        return render(request, 'blog/post/list.html', {'posts': posts, 'form_post': form_post})
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request, username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('blog:post_list')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'blog/post/list.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('blog:post_list')


@login_required
def post_detail(request, post_pk, post_slug):
    post = get_object_or_404(Post, id=post_pk, slug=post_slug)
    return render(request, 'blog/post/detail.html', {'post': post})


# лента новостей
@login_required
def news_list(request):
    user_list = []
    read = []
    followers = Contact.objects.filter(user_from=request.user)
    for u in followers:
        user_list.append(u.user_to)      
    followers_posts = Post.objects.filter(author__in=user_list)
    reads = User.objects.values('posts_readers').filter(id=request.user.id)   
    for r in reads:
        read.append(r['posts_readers'])
    return render(request, 'blog/post/news_list.html', {'followers_posts': followers_posts, 'read': read})


# отмечаем пост прочитанным
@login_required
def add_reading(request, post_id):
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
            post.users_readers.add(request.user)
            return redirect('blog:news_list')
        except:
            pass
    return redirect('blog:news_list')

