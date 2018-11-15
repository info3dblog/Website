from posts.views import detail
from django.shortcuts import get_object_or_404
from .models import FriendlyUrl

def getdetails(request, post_slug):
    post_id = get_object_or_404(FriendlyUrl, slug=post_slug).post.id
    detail(request, post_id)
