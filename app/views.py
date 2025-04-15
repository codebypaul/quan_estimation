from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World')
    return render(request, 'home.html', context={}, status=200)


# def builders

# estimate form
def estimate_form(request):
    return render(request,'forms/estimate_form.html',context={},status=200)

# pricing
def builder_info(request):
    context={}
    return render(request,'info/builder_info.html',context=context,status=200)

def manufacturer_pricing(request):
    context = {
        'manufacturer': 'Moen' 
    }
    return render(request,'pricing/manufacturer_pricing.html',context=context,status=200)