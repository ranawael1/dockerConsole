from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
    
    # restframework APIs
    path('api/add-container', views.AddContainer, name='delete-container'),
    path('api/delete-container/<id>', views.delContainer, name='delete-container'),
    path('api/show-containers', views.showContainers, name='show-containers'),




]