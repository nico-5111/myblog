from django.shortcuts import render
from django.http import HttpResponse
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"t_home.html",{})
def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contact Page</h1>")
def about_view(request,*args,**kwargs):
    my_context={
        "my_text":"This is about us",
        "my_number":123,
        "my_list":[1,2,3,4,5,6]
    }
    return render(request,"t_about.html",my_context)
# Create your views here.
