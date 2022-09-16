import site
from django.contrib import admin
from authentication.models import User
from blog.models import Photo,Blog
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(User)
