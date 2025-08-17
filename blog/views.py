from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    """
    The Blog Hompage
    """
    # Get the last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    # Add context variable "latest_posts"
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/home.html', context)
