from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login),
    path('', views.home, name='home'),
    path('logout/', views.exit, name='exit'),
    path('insert/', views.insert, name='insert'),
    path('perfil/', views.perfil, name='perfil'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('eliminar/<id>', views.eliminarArt),
    path('eliminarvnt/<id>', views.eliminarVent),
    path('editar/<id>', views.editar),
    path('añadirestado/', views.añadirestado),
    path('editarVent/<id>', views.editarVent),
    path('editarplataforma/<id>', views.editarplataforma, name='editarplataforma'),
    path('editarArt/<id>', views.editarArt),
    path('editarVentdata/<id>', views.editarVentdata),
    path('editarplataformadata/<id>', views.editarplataformadata, name='editarplataformadata'),
    path('ventas/', views.ventas, name='ventas'),
    path('ventasdata/', views.ventaslg, name='ventasdata'),
    path('fotoperfil/', views.fotoperfil, name='fotoperfil'),
    path('ventasagg/', views.ventasagg, name='ventasagg'),
    path('ventaslist/', views.ventalist, name='ventaslist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)