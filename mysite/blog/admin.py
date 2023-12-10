from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ('status','categories')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)