from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.home, name='home'),
    path('logout/', views.exit, name='exit'),
    path('insert/', views.insert, name='insert'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('eliminar/<id>', views.eliminarArt),
    path('eliminarvnt/<id>', views.eliminarVent),
    path('editar/<id>', views.editar),
     path('editarVent/<id>', views.editarVent),
    path('editarplataforma/<id>', views.editarplataforma, name='editarplataforma'),
    path('editarArt/<id>', views.editarArt),
    path('editarVentdata/<id>', views.editarVentdata),
    path('editarplataformadata/<id>', views.editarplataformadata, name='editarplataformadata'),
    path('ventas/', views.ventas, name='ventas'),
    path('ventasdata/', views.ventaslg, name='ventasdata'),
    path('ventasagg/', views.ventasagg, name='ventasagg'),
    path('ventaslist/', views.ventalist, name='ventaslist'),
]