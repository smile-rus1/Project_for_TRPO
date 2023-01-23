from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class Index(View):
    def get(self,requests,*args,**kwargs):
        return HttpResponse("Hello world!")


