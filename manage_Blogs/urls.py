from django.urls import path

from . import views

app_name = 'manage_Blogs'
urlpatterns = [
    # /blogs/
    path('blogs/', views.index, name='blogs'),
    # /blogs/1
    path('blogs/<int:blogId>/', views.blogDetail, name='blogDetail'),
    path('blogs/<int:blogId>/createComment/', views.createComment, name='createComment'),
    path('blogs/create/', views.createBlog ,name='createBlog'),
    path('blogs/<int:blogId>/edit/', views.editBlog, name='editBlog'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout')
]