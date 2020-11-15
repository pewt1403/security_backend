from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .models import Blog, Comment


# Create your views here.
def homePage(request):
    return HttpResponseRedirect(reverse("manage_Blogs:blogs"))


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("manage_Blogs:blogs"))
        else:
            return HttpResponseRedirect(reverse("manage_Blogs:login"))
    context = {}
    return render(request, "manage_Blogs/login.html", context)


def index(request):
    orderedBlogList = Blog.objects.order_by("-pub_date")
    template = loader.get_template("manage_Blogs/index.html")
    context = {
        "orderedBlogList": orderedBlogList,
        "user": request.user,
    }
    return HttpResponse(template.render(context, request))


def blogDetail(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    comments = blog.comment_set.all().order_by("id")
    context = {"blog": blog, "comments": comments}
    return render(request, "manage_Blogs/detail.html", context)


@login_required(login_url="manage_Blogs:login")
def createBlog(request):
    # POST create
    if request.method == "POST" and request.user.is_authenticated:
        title = request.POST["title"]
        content = request.POST["content"]
        blog = Blog(title=title, content=content, owner=request.user)
        blog.save()
        return HttpResponseRedirect(reverse("manage_Blogs:blogDetail", args=(blog.id,)))
    # GET get form
    context = {}
    return render(request, "manage_Blogs/createBlog.html", context)


@login_required(login_url="manage_Blogs:login")
def editBlog(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    if (not request.user.is_superuser) and (blog.owner_id != request.user.id):
        return HttpResponseForbidden()
    # POST edit
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.edited = True
        blog.save()
        return HttpResponseRedirect(reverse("manage_Blogs:blogDetail", args=(blog.id,)))
    # GET page
    context = {"user": request.user, "blog": blog}
    return render(request, "manage_Blogs/editBlog.html", context)


@login_required(login_url="manage_Blogs:login")
def createComment(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    # POST create
    if request.method == "POST":
        comment_value = request.POST["comment"]
        comment = Comment(comment=comment_value, Blogs=blog, owner=request.user)
        comment.save()
    return HttpResponseRedirect(reverse("manage_Blogs:blogDetail", args=(blog.id,)))


@login_required(login_url="manage_Blogs:login")
def editComment(request, blogId, commentId):
    blog = get_object_or_404(Blog, pk=blogId)
    comment = get_object_or_404(Comment, pk=commentId)
    if (not request.user.is_superuser) and (comment.owner_id != request.user.id):
        return HttpResponseForbidden()
    # POST edit
    if request.method == "POST":
        comment.comment = request.POST["comment"]
        comment.edited = True
        comment.save()
        return HttpResponseRedirect(reverse("manage_Blogs:blogDetail", args=(blog.id,)))

    return HttpResponseRedirect(reverse("manage_Blogs:blogDetail", args=(blog.id,)))


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse("manage_Blogs:blogs"))
    return HttpResponseRedirect(reverse("manage_Blogs:blogs"))
