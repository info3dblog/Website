from django.http import HttpResponse
from .models import Post
from django.template import loader

def home(request):
	return HttpResponse("""<h1>Info3DBlog</h1><p>This is a text to test</p>""")

def index(request):
    latest_posts_list = Post.objects.order_by('-id')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_posts_list': latest_posts_list,
	}
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    return HttpResponse("You're looking at question %s." % post_id)
