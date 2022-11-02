from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def welcome(request):
  user_data={'insert_me':"here will be the data of users"}
  return render(request,'user.html',context=user_data)


