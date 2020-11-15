from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone

from .models import Blog, Comment

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('manage_Blogs:blogs'))
        else:
            return HttpResponseRedirect(reverse('manage_Blogs:login'))
    context = {}
    return render(request,'manage_Blogs/login.html',context)

def index(request):
    # print(request.user.username)
    orderedBlogList = Blog.objects.order_by('-pub_date')[:5]
    template = loader.get_template('manage_Blogs/index.html')
    context = {
        'orderedBlogList': orderedBlogList,
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))

def blogDetail(request, blogId):
    try:
        blog = Blog.objects.get(pk=blogId)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    context = {
        'blog': blog,
    }
    return render(request, 'manage_Blogs/detail.html', context)

@login_required(login_url='manage_Blogs:login')
def createBlog(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog.create(title=title,content=content,creator=request.user.username)
        blog.save()
        return HttpResponseRedirect(reverse('manage_Blogs:blogDetail', args=(blog.id,)))
    context = {}
    return render(request,'manage_Blogs/createBlog.html',context)

@login_required(login_url='manage_Blogs:login')
def editBlog(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.pub_date= timezone.now()
        blog.edited = True
        blog.save()
        return HttpResponseRedirect(reverse('manage_Blogs:blogDetail', args=(blog.id,)))
    if blog.creator == request.user.username:
        context = {
            'user': request.user,
            'blog':blog
        }
        return render(request,'manage_Blogs/editBlog.html',context)
    return HttpResponseRedirect(reverse('manage_Blogs:blogDetail', args=(blog.id,)))

@login_required(login_url='manage_Blogs:login')
def deleteBlog(request, blogId):
    return

@login_required(login_url='manage_Blogs:login')
def createComment(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    comment = Comment.create(comment=request.POST['comment'],blogId=blog,creator=request.user.username)        
    comment.save()
    return HttpResponseRedirect(reverse('manage_Blogs:blogDetail', args=(blog.id,)))
 

@login_required(login_url='manage_Blogs:login')
def editComment(request):
    return

@login_required(login_url='manage_Blogs:login')
def deleteComment(request):
    return

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('manage_Blogs:blogs'))
    return HttpResponseRedirect(reverse('manage_Blogs:blogs'))