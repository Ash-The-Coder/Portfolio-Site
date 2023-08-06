from django.views.generic import TemplateView, RedirectView
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.create_blog_post, name='create-blog-post'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/profile/', TemplateView.as_view(template_name='homepage.html'), name='profile_redirect'),
    path('categories/', views.categories_list, name='categories_list'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('projects/', views.projects_list, name='projects_list'),
]

