from django.http import HttpResponse
from .models import Post
from django.template import loader
import markdown
from django.shortcuts import get_object_or_404


def home(request):
    return HttpResponse(
        """
		<h1>Info3DBlog</h1>
		""")


def index(request):
    latest_posts_list = Post.objects.order_by('-id')[:5]
    template = loader.get_template('posts/index.html')
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	template = loader.get_template('posts/detail.html')
	return HttpResponse(template.render({ 'post': post }, request))
