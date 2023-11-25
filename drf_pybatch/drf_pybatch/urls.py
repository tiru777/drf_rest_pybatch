"""
URL configuration for drf_pybatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Function based views @api_view
    path('emp_list',employee_list_post),
    path('emp_detail/<int:id>/',employee_detail,name='employee-detail'),

    # Class Based Views API View
    path('emp_list_m',EmployeeList.as_view()),
    path('emp_detail_model/<int:id>/',EmployeeDetail.as_view()),

    # Class based View with Hyper linked serializer and mixins
    path('emp_list_hyper',EmployeeListHyper.as_view()),
    path('emp_list_hyp_detail/<int:pk>/', EmployeeDetailHyper.as_view()),

    # Class Based View with generics

    path('emp_list_generic',EmployeeListLc.as_view()),
    path('emp_detail_generic/<int:pk>/',EmployeeDetailRUD.as_view())

]
