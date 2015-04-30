from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Post

# Create your views here.
def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	template = loader.get_template('blog/index.html')
	context = Context({'latest_posts': latest_posts, })
	return HttpResponse(template.render(context))