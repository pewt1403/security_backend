from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Blog, Comment

# Create your views here.
def index(request):
    orderedBlogList = Blog.objects.order_by('-pub_date')[:5]
    template = loader.get_template('manage_Blogs/index.html')
    context = {
        'orderedBlogList': orderedBlogList,
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

def createComment(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    comment = Comment.create(request.POST['comment'],blog)        
    comment.save()
    return HttpResponseRedirect(reverse('manage_Blogs:blogDetail', args=(blog.id,)))

def createBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog.create(title=title,content=content)
        blog.save()
        return HttpResponseRedirect(reverse('manage_Blogs:blogDetail', args=(blog.id,)))
    context = {}
    return render(request,'manage_Blogs/createBlog.html',context)