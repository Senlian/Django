from django.shortcuts import render, redirect
from django.shortcuts import reverse, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from common.gen_verify import draw_img
from .forms import UserInfoHandlerForm
from .models import UserInfoHandler, RedisHandler


# Create your views here.

def indexpage(request):
    return render(request, 'WebRedis/index.html', {'username': request.session.get('username', None)})


def registerpage(request):
    if request.method.lower() == 'post':
        return render(request, 'WebRedis/register.html')
    else:
        verify(request)
        return render(request, 'WebRedis/register.html')


def register(request):
    if request.method.lower() == 'post':
        # 是否注册成功
        is_ok = False
        postForm = UserInfoHandlerForm(request.POST)
        if postForm.is_valid():
            formData = postForm.cleaned_data
            uid = formData.get('uid', None)
            pwd = formData.get('pwd', None)
            repwd = formData.get('repwd', None)
            name = formData.get('name', None)
            phone = formData.get('phone', None)
            email = formData.get('email', None)
            verify_code = formData.get('verify', None)
            verify_session = request.session.get('verify', None).lower()

            if pwd != repwd:
                postForm.add_error('repwd', "两次输入密码不一致")
            if verify_code != verify_session:
                postForm.add_error('verify', "验证码错误")
            # 数据保存
            if postForm.is_valid():
                pop_keys = set(formData.keys()).difference((field.name for field in UserInfoHandler._meta.fields))
                for pop_key in pop_keys:
                    formData.pop(pop_key)
                # 保存注册信息
                addUser = UserInfoHandler.objects.create(**formData)

                addUser.save()
                is_ok = True
                return JsonResponse({'is_ok': is_ok})
        if not is_ok:
            postForm.errors.update({'is_ok': is_ok})
            return JsonResponse(postForm.errors)
    else:
        verify(request)
        registerForm = UserInfoHandlerForm()
        return render(request, 'WebRedis/new_register.html', context=locals())


def loginpage(request):
    if request.method.lower() == 'post':
        username = request.POST.get('username', None)
        passwd = request.POST.get('passwd', None)
        verify_in = request.POST.get('verify', None).lower()
        verify_code = request.session.get('verify', None).lower()
        if verify_in == verify_code:
            request.session['username'] = username
            return redirect('WebRedis:index')
        else:
            verify(request)
            return render(request, 'WebRedis/login.html')
    else:
        verify(request)
        return render(request, 'WebRedis/login.html')


def logoutpage(request):
    # 删除session
    auth.logout(request)
    return redirect('WebRedis:login')


def verify(request):
    request.session['verify'] = draw_img()
    return JsonResponse({'refresh': 'ok'})


def demo(request):
    return render(request, 'WebRedis/demo.html')
