"""photoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import loginViews,selectFollows, logout,registerView,changeProfil
import blog
from blog.views import UploadBlogPhoto, home_view, multiplePhotoView,  upd_del_blog,upload_photo_view
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView

from photoblog.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/old_login/',loginViews.as_view(),name='old_login'),
    path('authentication/login/',LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ),name='login'),
    path('authentication/old_logout/',logout,name='old_logout'),
    path('authentication/logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('authentication/changepasseword/',PasswordChangeView.as_view(
        template_name='authentication/change_password.html',
        success_url='home'
    ),name='changepasseword'),
    path('authentication/register/',registerView.as_view(),name='register'),
    path('authentication/changepp',changeProfil,name='change_pp'),
    path('blog/home/',home_view,name='home'),
    path('blog/photo/upload/',upload_photo_view,name='upload_photo'),
    path('blog/create_blog',UploadBlogPhoto.as_view(),name='createBlogPhoto'),
    path('blog/update_delete/<int:blog_id>',upd_del_blog,name='upd_del'),
    path('blog/photo/multiple_photo',multiplePhotoView,name='multiple_photo'),
    path('blog/follows',selectFollows,name='follows'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
