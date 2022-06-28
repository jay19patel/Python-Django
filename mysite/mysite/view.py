# i have create this file

# code for video simple 


from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render (request,'index.html')

# def ind(request):
#     return HttpResponse ("MY webs")


