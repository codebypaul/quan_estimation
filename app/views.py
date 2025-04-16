from django.shortcuts import render
from django.http import HttpResponse

from .models import Builder,Moen,Delta
# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World')
    return render(request, 'home.html', context={}, status=200)


# def builders

# estimate form
def estimate_form(request):
    return render(request,'forms/estimate_form.html',context={},status=200)

def spreadsheet_builder_form(request):
    context={

    }
    return render(request,'forms/spreadsheet_builder_form.html',context=context,status=200)


def builder_info(request):
    builders = Builder.objects.all()
    context={
        'builders':builders,
    }
    return render(request,'info/builder_info.html',context=context,status=200)

def builder_info_form(request):
    context={}
    return render(request,'forms/builder_info_form.html',context=context,status=200)

# pricing
def manufacturer_pricing(request):
    moen_catalog = Moen.objects.all()
    delta_catalog = Delta.objects.all()
    context = {
        'moen_catalog':moen_catalog,
        'delta_catalog':delta_catalog,
    }
    return render(request,'pricing/manufacturer_pricing.html',context=context,status=200)

def china_and_tubs(request):
    context={

    }
    return render(request,'info/china_tubs.html',context=context,status=200)

def labor_costs(request):
    context={
        
    }
    return render(request,'info/labor_pricing.html',context=context,status=200)