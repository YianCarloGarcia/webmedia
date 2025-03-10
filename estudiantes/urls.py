from django.urls import path 
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.principal, name='principal'),
    path('lineas', views.lineas, name='lineas'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('nuevo', views.nuevo, name='nuevo'),
    path('guardarQr', views.guardarQr, name='guardarQr'),
    path('success', views.success, name='success'),
    path('contar', views.contarQr, name='contar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)