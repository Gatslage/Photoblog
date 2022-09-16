from django.contrib import admin
from blog.models import Photo,Blog, interBlogUser

# Register your models here.
admin.site.register(Photo)
admin.site.register(Blog)

admin.site.register(interBlogUser)