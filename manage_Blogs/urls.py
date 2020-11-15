from django.urls import path

from manage_Blogs.views import homePage

from . import views

app_name = "manage_Blogs"
urlpatterns = [
    # /
    path("", views.homePage, name="home"),
    # /blogs/
    path("blogs/", views.index, name="blogs"),
    # /blogs/1
    path("blogs/<int:blogId>/", views.blogDetail, name="blogDetail"),
    path("blogs/create/", views.createBlog, name="createBlog"),
    path("blogs/<int:blogId>/delete/", views.deleteBlog, name="deleteBlog"),
    path(
        "blogs/<int:blogId>/createComment/", views.createComment, name="createComment"
    ),
    path("blogs/<int:blogId>/edit/", views.editBlog, name="editBlog"),
    path(
        "blogs/<int:blogId>/edit/<int:commentId>/",
        views.editComment,
        name="editComment",
    ),
    path("blogs/<int:blogId>/delete/<int:commentId>/", views.deleteComment, name="deleteComment"),
    
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
]
