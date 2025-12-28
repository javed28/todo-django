from django.urls import path
from . import views

urlpatterns = [
    path('employeeView/',views.EmployeeView)
]
