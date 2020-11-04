"""student_portel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from studentapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.student_register,name='student_register'),
    path('student_register_details/',views.student_register,name='student_register_details'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_login_details/',views.student_login,name='student_login_details'),
    path('hr_list/',views.Hr_list,name='hr_list'),
    path('hr_datails/',views.hr_datails,name='hr_datails'),
    path('notification/',views.Notification,name='notification'),

]
