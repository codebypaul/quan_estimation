from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.hello_world),
    path('build_estimate/',views.estimate_form),
]