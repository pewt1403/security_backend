from django.urls import path

from . import views

app_name = 'authen'
urlpatterns = [
    # /blogs/
    #path('', views.index, name='index'),
    # /blogs/1
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]