from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.home, name='home'),
    path('logout/', views.exit, name='exit'),
    path('insert/', views.insert, name='insert'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('eliminar/<id>', views.eliminarArt),
    path('editar/<id>', views.editar),
    path('editarplataforma/<id>', views.editarplataforma, name='editarplataforma'),
    path('editarArt/<id>', views.editarArt),
    path('editarplataformadata/<id>', views.editarplataformadata, name='editarplataformadata'),
    path('ventas/', views.ventas, name='ventas'),
    path('ventasdata/', views.ventaslg, name='ventasdata'),
    path('ventasagg/', views.ventasagg, name='ventasagg'),
]