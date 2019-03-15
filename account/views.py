from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import UserInfo, UserProfile
from .form import LoginForm, RegisterForm, UserProfileForm, UserForm, UserInfoForm


# Create your views here.

def user_login(request):
    if request.method.upper() == 'GET':
        login_form = LoginForm()
        print(dir(login_form))
        return render(request, 'account/login.html', {'login_form': login_form})

    if request.method.upper() == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            userinfo = login_form.cleaned_data
            # TODO : 调用django内置用户验证方法
            user = authenticate(username=userinfo.get('username', ''), password=userinfo.get('password', ''))
            if user:
                # TODO: 保存session
                login(request, user)

                print(dict(request.session))
                # return HttpResponse(LoginForm())
                return redirect('blog:blog_title')
            else:
                return HttpResponse('not login')
        else:
            return HttpResponse('invalid login')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            # commit=False，暂不保存数据库
            new_user = user_form.save(commit=False)
            # 校验数据
            new_user.set_password(user_form.cleaned_data['password'])
            # 保存
            new_user.save()

            new_userprofile = userprofile_form.save(commit=False)
            new_userprofile.user = new_user
            new_userprofile.save()
            login(request, new_user)
            UserInfo.objects.create(user=new_user)
            return redirect('blog:blog_title')
        else:
            return HttpResponse('register failed!')
    user_form = RegisterForm()
    userprofile_form = UserProfileForm()
    return render(request, 'account/register.html', {'form': user_form, 'userprofile_form': userprofile_form})


@login_required(login_url=reverse_lazy('account:user_login'))
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, 'account/myself.html', {'user': user, 'userprofile': userprofile, 'userinfo': userinfo})


@login_required(login_url=reverse_lazy('account:user_login'))
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * user_profile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = user_profile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userinfo.save()
            userprofile.save()
            return HttpResponseRedirect(reverse_lazy('account:user_info'))
            # return redirect("account:user_info")

    user_form = UserForm(instance=request.user)
    user_profile_form = UserProfileForm(initial={'birth': userprofile.birth, 'phone': userprofile.phone})
    # user_profile_form = UserProfileForm(instance=userprofile)
    # userinfo_form = UserInfoForm(instance=userinfo)
    userinfo_form = UserInfoForm(
        initial={'school': userinfo.school, 'company': userinfo.company, 'profession': userinfo.profession,
                 'address': userinfo.address, 'aboutme': userinfo.aboutme})
    return render(request, 'account/myself_edit.html',
                  {'user_form': user_form, 'user_profile_form': user_profile_form, 'userinfo_form': userinfo_form})


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def my_image(request):
    if request.method == 'POST':
        img = request.POST.get('img', '')
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return redirect('account:user_info')
    return render(request, r'account/imgCrop.html')
