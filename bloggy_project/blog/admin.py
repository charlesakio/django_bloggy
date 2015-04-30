from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	"""
	Customize admin site by listing Post models
	title and created_at
	"""
	list_display = ('title', 'created_at')


#Register classes to the Django admin interface
admin.site.register(Post, PostAdmin)