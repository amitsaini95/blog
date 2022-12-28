from django.shortcuts import HttpResponse,render
class my_middlewares:
    def __init__(self,get_response):
        self.get_response=get_response 
    

         
    def __call__(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return render(request,'blog/post_list.html')
            
        else:
         response= HttpResponse("<h1>invalid ip address</h1>")
         return response
  