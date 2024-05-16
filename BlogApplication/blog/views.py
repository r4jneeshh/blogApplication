from django.shortcuts import render
from django.utils import timezone
from .models import Post


def postList(request):
    # Fetch posts that are published (publishedDate less than or equal to the current time)
    posts = Post.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')

    # Render the 'postList.html' template with the posts context
    return render(request, 'blog/postList.html', {'posts': posts})
