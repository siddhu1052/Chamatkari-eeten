"""
URL configuration for prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from bricks import views
from django.conf import settings  
from django.urls import path, include  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.Login,name='login'),
    path('signup',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('land_details',views.land_details,name='land_details'),
    path('built_details',views.built_details,name='built_details'),
    path('properties',views.properties,name='properties'),
    path('property_details/<str:property_id>/',views.property_details,name='property_details'),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

