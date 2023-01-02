from django.shortcuts import HttpResponse
from .models import *
class my_middlewares:
    def __init__(self,get_response):
        self.get_response=get_response
 
    def __call__(self,request):
        host=request.META['HTTP_HOST']
        ip=Ip.objects.filter(Ip_address=host[:-5])
        if ip:
            response=self.get_response(request)
            return response
        else:
            return HttpResponse("<h1>invalid ip address</h1>")