from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

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
    moen_paginator = Paginator(moen_catalog,20)
    moen_page_num = request.GET.get('page')
    moen_page_obj = moen_paginator.get_page(moen_page_num)

    delta_catalog = Delta.objects.all()
    delta_paginator = Paginator(delta_catalog,20)
    delta_page_num = request.GET.get('page')
    delta_page_obj = delta_paginator.get_page(delta_page_num)

    page_number = request.GET.get('page')
    

    context = {
        'moen_catalog':moen_catalog,
        'moen_page_obj':moen_page_obj,
        'delta_catalog':delta_catalog,
        'delta_page_obj':delta_page_obj,
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