from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    context={
        'a':'vineet'
    }
    return render(request,'home.html',context)
    # return HttpResponse("this is homepage")
def about(request):
    return HttpResponse("this is about page")
def contact(request):
    return HttpResponse("vkwilson")

