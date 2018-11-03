from django.http import HttpResponse
from .models import Post, Category
from django.template import loader
import markdown
from django.shortcuts import get_object_or_404


def home(request):
    latest_posts_list = Post.objects.order_by('-id')[:5]
    template = loader.get_template('posts/home.html')
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    posts_list = Post.objects.order_by('title')
    categories_list = Category.objects.order_by('title')
    template = loader.get_template('posts/index.html')
    context = {
        'posts_list': posts_list,
        'categories_list': categories_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	template = loader.get_template('posts/detail.html')
	return HttpResponse(template.render({ 'post': post }, request))
