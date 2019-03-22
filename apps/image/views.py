from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from .models import Image
from .forms import ImageForm
from django.conf import settings
from sorl.thumbnail import delete as sorl_thumbnail_del



# Create your views here.

@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
@require_POST
def upload_image(request):
    image_form = ImageForm(request.POST)
    try:
        if image_form.is_valid():
            new_img = image_form.save(commit=False)
            new_img.author = request.user
            new_img.save()
            return JsonResponse({'status': '1'})
    except Exception as e:

        return JsonResponse({'status': '0'})
    print(image_form.errors)
    return JsonResponse({'status': '2'})


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def list_images(request):
    imags = Image.objects.filter(author=request.user)
    return render(request, 'images/list_images.html', {'imags': imags})


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def edit_image(request, image_id):
    return HttpResponse('image_id={}'.format(image_id))


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def del_image(request):
    image_id = request.POST.get('image_id')
    try:
        image = Image.objects.get(id=int(image_id))
        import os
        image.delete()
        # print(image.image.path)
        # print(image.image.name)

        sorl_thumbnail_del(image.image.name)


        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('2')
