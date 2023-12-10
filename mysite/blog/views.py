from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import generic
from .models import Post, Category
from .forms import BlogPostForm

def is_superuser(user):
    return user.is_superuser

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

@user_passes_test(is_superuser)
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the desired URL after successful submission
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})


def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = category.posts.filter(status=1)  # Display only published posts

    context = {
        'category': category,
        'posts': posts,
    }

    return render(request, 'category_posts.html', context)

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def projects_list(request):
    projects_category = Category.objects.get(name='Project')
    projects = projects_category.posts.all()  # Assuming you have a related_name='posts' in your Category model
    return render(request, 'projects.html', {'projects': projects})

