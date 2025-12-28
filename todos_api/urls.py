from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employeesViewSet',views.EmployeeViewSet,basename='employeeviewSet')
router.register('employeesModelViewSet',views.EmployeeModelViewSet,basename='employeeModelSet')

urlpatterns = [
    path('todosView/',views.todosView),
    path('todosDetailView/<int:pk>/',views.todosDetailView),
    #class based view
    path('employees/',views.Employees.as_view()),
    path('employeeDetailView/<int:pk>/',views.EmployeeDetailView.as_view()),
    path('employeesMixin/',views.employeesMixin.as_view()),
    path('employeeDetailViewMixin/<int:pk>/',views.employeeDetailViewMixin.as_view()),
    path('employeesGenericsMixin/',views.employeesGenericsMixin.as_view()),
    path('employeesDetailsGenericsMixin/<int:pk>/',views.employeesDetailsGenericsMixin.as_view()),
    path('',include(router.urls)),
]

