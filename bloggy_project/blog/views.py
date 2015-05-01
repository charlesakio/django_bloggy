from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import get_object_or_404

from blog.models import Post

# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	template = loader.get_template('blog/index.html')
	context = Context({'latest_posts': latest_posts, })
	return HttpResponse(template.render(context))

def post(request, post_id):
	single_post = get_object_or_404(Post, pk=post_id)
	template = loader.get_template('blog/post.html')
	context = Context({'single_post': single_post, })
	return HttpResponse(template.render(context))
