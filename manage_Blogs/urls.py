from django.urls import path

from . import views

app_name = 'manage_Blogs'
urlpatterns = [
    # /blogs/
    path('blogs/', views.index, name='blogs'),
    # /blogs/1
    path('blogs/<int:blogId>/', views.blogDetail, name='blogDetail'),
    path('blogs/create/', views.createBlog ,name='createBlog'),
    path('blogs/createComment/<int:blogId>/', views.createComment, name='createComment'),
    path('blogs/edit/<int:blogId>/', views.editBlog, name='editBlog'),
    path('blogs/edit/<int:blogId>/<int:commentId>/', views.editComment, name='editComment'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout')
]