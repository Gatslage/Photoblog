from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from authentication.forms import followForm, loginForm, profilForm,registerForm
from authentication.models import User
from django.contrib.auth import authenticate,login as login_auth,logout as logout_auth
from django.views.generic import View
from django.conf import settings

from blog.forms import PhotoForm, blogForm


def login(request):
    us=loginForm()
    message=None
    if request.method=='POST':
        myF=loginForm(request.POST)
        if myF.is_valid():
            connect=authenticate(request,username=myF.cleaned_data['username'],password=myF.cleaned_data['password'])
            print('ggggggggggggggggggggggg')
            print(connect.password)
            if connect is not None:
                login_auth(request, connect)
                message=f'bienvenue {connect.username}'
                return redirect('home')
            else:
                message='Identifiant invalides'
            
    return render(request,'authentication/login.html',{'form':us,'message':message})
# Create your views here.

class loginViews(View):
    template_page='authentication/login.html'
    form_class=loginForm
    
    def get(self,request):
        message=''
        form_page=self.form_class()
        return render(request,self.template_page,{'form':form_page,'message':message})
    def post(self,request):
        form_page=self.form_class(request.POST)
        if form_page.is_valid():
            user=authenticate(username=form_page.cleaned_data['username'],password=form_page.cleaned_data['password'])
            if user is not None :
                login_auth(request,user)
                message=''
                return redirect('home')
            else:
                message='utilisateur invalide'
        return render(request,self.template_page,{'form':form_page,'message':message})
    
class registerView(View):
    template_page='authentication/register.html'
    form_class=registerForm
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_page,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save()
            login_auth(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request,self.template_page,{'form':form})
def changeProfil(request):
    form=profilForm(instance=request.user)
    if request.method=='POST':
         
        if profilForm(request.POST,request.FILES).is_valid():
            form =profilForm(request.POST,request.FILES,instance=request.user)
            user=form.save()
            return redirect('login')
    return render(request,'authentication/change_profil.html',{'form':form})


        
        
def logout(request):
    logout_auth(request)
    return redirect('login')

def selectFollows(request):
    form=followForm(instance=request.user)
    if request.method=='POST':
        form=followForm(request.POST,instance=request.user)
        if form.is_valid():
            follows=form.save()
            return redirect('home')
    return render(request,'blog/follows.html',context={'form':form})
        