from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
# Create your views here.



def welcome(request):
  users_list = User.objects.all()
  user_data={'user_data':users_list}
  return render(request,'user.html',context=user_data)


