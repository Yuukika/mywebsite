from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm,RegisterForm,ProfileForm
from django.core.urlresolvers import reverse
from .models import Profile
from django.contrib.auth.models import User

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request,user)
                #return HttpResponseRedirect(reverse('article:home_page'))
                #return HttpResponse('welcome')
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponse('wrong username or password')
        else:
            return HttpResponse('invalid login')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'account/login.html',{'form':login_form})


def register(request):
    if request.method == "POST":
        registerform = RegisterForm(data=request.POST)
        if registerform.is_valid():
            new_user = registerform.save(commit=False)
            new_user.set_password(registerform.cleaned_data['password'])
            new_user.save()
            return HttpResponse('成功注册')
        else:
            return HttpResponse('不能注册')
    else:
        registerform = RegisterForm()
        return render(request, 'account/register.html',{'form':registerform})

def profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
        print("baidubaidubaidu")
    except:
        Profile.objects.create(user=request.user)
        user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profileform = ProfileForm(data=request.POST)
        if profileform.is_valid():
            cd = profileform.cleaned_data
            user_profile.bio = cd['bio']
            user_profile.location = cd['location']
            user_profile.save()
            return HttpResponseRedirect('/account/profile/')
            #return HttpResponse("修改成功")
        else:
            return HttpResponse('修改失败')
    else:
        profileform = ProfileForm()
        return render(request, 'account/profile.html',{"form":profileform,'profile':user_profile})










