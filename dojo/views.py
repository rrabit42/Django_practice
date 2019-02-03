import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Post
from .Forms import PostForm


def generate_view_fn(model):
    def view_fn(request, id):
        instance = get_object_or_404(model, id=id)
        instance_name = model._meta.model_name
        template_name='{}/{}_detail.html'.format(model._meta.app_label, instance_name)
        return render(request, template_name, {
            instance_name: instance,
        })
    return view_fn

post_detail = generate_view_fn(Post)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form
    })


def mysum(request, numbers):
    # numbers = "1/2/12/123/12312/312/123123"
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'. format(name,age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango<h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name':name})


def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬&장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS']
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = 'C:\dev\\askdjango\\useforpractice.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'useforpractice.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Diposition'] = 'attachment'; filename="{}".format(filename)
        return response

