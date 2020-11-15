from django.urls import path

from . import views

app_name = 'manage_Blogs'
urlpatterns = [
    # /blogs/
    path('', views.index, name='index'),
    # /blogs/1
    path('<int:blogId>/', views.blogDetail, name='blogDetail'),
    path('<int:blogId>/createComment/', views.createComment, name='createComment'),
    path('create/', views.createBlog ,name='creatBlog'),
]