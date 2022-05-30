"""d05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('ex00/', include(('ex00.urls', "ex00"), namespace='ex00')),
    # path('ex01/', include(('ex01.urls', "ex01"), namespace='ex01')),
    path('ex02/', include(('ex02.urls', "ex02"), namespace='ex02')),
    path('ex03/', include(('ex03.urls', "ex03"), namespace='ex03')),
    path('ex04/', include(('ex04.urls', "ex04"), namespace='ex04')),
    path('ex05/', include(('ex05.urls', "ex05"), namespace='ex05')),
    path('ex06/', include(('ex06.urls', "ex06"), namespace='ex06')),
    path('ex07/', include(('ex07.urls', "ex07"), namespace='ex07')),
]
