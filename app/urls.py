from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.hello_world),
    path('build_estimate/',views.estimate_form, name='estimate_builder'),
    path('builder_spreadsheet/',views.estimate_form, name='spreadsheet_builder'),
    
    # pricing
    path('builder_info/',views.builder_info, name='builder_info'),
    path('manufacturer_pricing/',views.manufacturer_pricing, name='manufacturer_pricing'),
]