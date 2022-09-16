from ast import Starred
from itertools import chain
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Photo,Blog
from django.views.generic import View
from django.forms import formset_factory

from blog.forms import PhotoForm, blogForm, deleteForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

@login_required
def home_view(request):
    blogs=Blog.objects.all()
    photos=Photo.objects.exclude(blog__in=blogs)
    blogs_photos=sorted(chain(blogs,photos),key=lambda instance:instance.date_created,reverse=True)
    paginator_source=Paginator(blogs_photos,6)
    page=request.GET.get('page')
    page_objet=paginator_source.get_page(page)
    return render(request,'blog/home.html',{'blogs_photos': page_objet})
@login_required
def upload_photo_view(request):
    form =PhotoForm()
    if request.method =='POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            print('image enregistrer')
            Pho= form.save(commit=False)
            Pho.uploader=request.user
            Pho.save()
            return redirect('home')
            
    return render(request,'blog/photoUpload.html',{'form':form})

class UploadBlogPhoto(View):
    template_page='blog/upload_blog_photo.html'
    context={
            'photoForm':PhotoForm(),
            'blogForm':blogForm()
        }
   
    def get(self,request):
        return render(request,self.template_page,context=self.context)
    
    def post(self,request):
        photoF=PhotoForm(request.POST,request.FILES)
        blogF=blogForm(request.POST)
        if all([photoF.is_valid(),blogF.is_valid()]):
            photo=photoF.save(commit=False)
            blog=blogF.save(commit=False)
            photo.uploader=request.user
            photo.save()
            blog.author=request.user
            blog.photo=photo
            blog.save()
            blog.contributions.add(request.user,through_defaults={'participation':'auteur principal'})
            return redirect('home')
        self.context['photoForm']=photoF
        self.context['blogForm']=blogF
        return render(request,self.template_page,self.context)
@login_required
def upd_del_blog(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    upd_blog=blogForm(instance=blog)
    del_blog=deleteForm()
    if request.method=='POST':
        if 'upd_blog' in request.POST:
            upd_blog=blogForm(request.POST,instance=blog)
            if upd_blog.is_valid():
                upd_blog.save()
        else:
            del_blog=deleteForm(request.POST)
            if del_blog.is_valid():
                blog.delete()
        return redirect('home')
        
    context={
        'upd_blog':upd_blog,
        'del_blog':del_blog
    }
    return render(request,'blog/upd_del_blog.html',context=context)
        
@login_required
def multiplePhotoView(request):
    multiPhotoForm=formset_factory(PhotoForm,extra=5)
    forms=multiPhotoForm()
    if request.method=='POST':
        forms=multiPhotoForm(request.POST,request.FILES)
        if forms.is_valid():
            for form in forms:
                if form.cleaned_data:        
                    photo=form.save(commit=False)
                    photo.uploader=request.user
                    photo.save()
            return redirect('home')
    return render(request,'blog/multiPhotos.html',context={'forms':forms})

