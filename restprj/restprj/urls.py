"""restprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers

from restapp.views import EmployeeViewset
from restapp.views import HomeView

router=routers.DefaultRouter()
router.register('',EmployeeViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('emp/', include(router.urls)),
    path('index/', HomeView.as_view(),name='index'),
=======
    path('emp/',include(router.urls)),
    path('index/',HomeView.as_view(),name='index'),

>>>>>>> 29bf8bf6f84c5797206169df8c8c338d1f82dad7
]
