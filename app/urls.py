from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.hello_world),
    path('build_estimate/',views.estimate_form, name='estimate_builder'),
    path('builder_spreadsheet/',views.spreadsheet_builder_form, name='spreadsheet_builder'),
    
    # pricing
    path('builder_info/',views.builder_info, name='builder_info'),
    path('manufacturer_pricing/',views.manufacturer_pricing, name='manufacturer_pricing'),
    path('china_and_tubs/',views.china_and_tubs, name='china_and_tubs'),
    path('labor_costs/',views.labor_costs, name='labor_costs'),
]