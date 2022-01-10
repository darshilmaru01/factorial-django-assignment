from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "input.html")

def fact(request):  

    num = request.POST['num']

    if num.isdigit():
        a = int(num)
        
        f = 1
        i = 1
        
        while i <= a:
            f = f * i
            i = i + 1

        
    #print(request)
    #import ipdb;ipdb.set_trace()

    return render(request, "result.html", {"result": f})
