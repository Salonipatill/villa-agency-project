"""
URL configuration for Villa project.

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
from VillaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('index/', views.index,name='index'),
    path('contact/', views.contact,name='contact'),
    path('properties/', views.properties,name='properties'),
    path('property-details/',views.properties_details,name='property'),
    path('registration/', views.registration,name='registration'),
    path('login/', views.login,name='login'),
    #path('userdtl/', views.userdtl,name='userdtl'),
    path("images/",views.image_upload,name="image_upload"),
    path("delete/<int:image_id>/",views.delete_image,name="delete_data"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)