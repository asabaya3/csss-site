from django.shortcuts import render
from django.views import generic

from .models import Post, Category, Announcement

class PostDetailView(generic.DetailView):
    model = Post

class PostListView(generic.ListView):
    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs['slug'])
    
class AnnouncementListView(generic.ListView):
    def get_queryset(self):
        return Announcement.objects.all().order_by('-created')[:5]
    