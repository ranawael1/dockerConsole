from django.http import HttpResponse
from django.shortcuts import render, redirect
from httplib2 import Response

from dockerConsole.serialzers import ContainersSerializer
from .models import Container

# authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# celery tasks
from .tasks import create_container, delete_container

# APIs
from rest_framework.decorators import api_view

# @authenticated_user
def loginUser(request):
    if request.method == 'POST':
        # gather the username and the password entered on the login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate the data entered by the user
        user = authenticate(request, username=username, password=password)
        # if the user exists
        if user is not None:
            login(request, user)
            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            else:
                # return redirect(request.META.get('HTTP_REFERER'), history = -2)  #to stay in the same page after logging in
                return redirect('home')
        # if the user not exists
        messages.info(request, 'Username or Password is incorrect')
    return render(request, 'docker-console/login.html')



# Logout
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

# console of user
@login_required(login_url='login')
def home(request):
    user = request.user
    context = {'user': user}
    return render(request,'docker-console/console.html', context)



## APIs

@api_view(['POST'])
def AddContainer(request):
    container_ser = ContainersSerializer(data=request.data)
    if container_ser.is_valid():
        container_ser.save()
        create_container.delay(request.data["name"], request.data["tag"])
        return Response(container_ser.data)



@api_view(['DELETE'])

def delContainer(request,id):
    container = Container.objects.get(image_id=id)
    container.delete()
    delete_container.delay(request.data["id"])
    return HttpResponse('container deleted')


@api_view(['GET'])
def showContainers(request):
    contaniers = Container.objects.filter(user=request.user)
    container_ser = ContainersSerializer(contaniers, many=True)
    return Response(container_ser.data)