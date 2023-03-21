from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Producto, Ventas, Clientes, Perfil
from django.contrib import messages
from django.conf import settings
from os import remove
from os import path
import os
from pathlib import Path

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  LOGIN    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Create your views here.
def login(request):
    return render(request, 'registration/login.html')

@login_required
def home(request):
    user = request.user.username
    print(user)
    homedata = Producto.objects.all().values('id','codigo_referencia', 'nombre', 'modelo', 'unidades', 'preciounidad', 'precioventa', 'envio')
    return render(request, 'inicio.html', {"Productos": homedata})

def exit(request):
    logout(request)
    return redirect('home')


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  DASHBOARD    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

@login_required
def insert(request):
    codigo_referencia = request.POST['codigo_referencia']
    nombre = request.POST['nombre']
    modelo = request.POST['modelo']
    unidades = request.POST['unidades']
    preciounidad = request.POST['preciounidad']
    precioventa = request.POST['precioventa']
    envio = request.POST['envio']
    precio = Producto.objects.filter(codigo_referencia=codigo_referencia).values('unidades').values_list('unidades', flat=True)
    if not precio:
        Insert = Producto.objects.create(codigo_referencia = codigo_referencia, nombre = nombre, modelo = modelo, unidades = unidades, preciounidad = preciounidad, precioventa = precioventa, envio = envio)
        return redirect('home')
    
    print("El codigo es: ",precio)
    preciodata = Producto.objects.get(codigo_referencia=codigo_referencia)
    for precios in precio:
        data = precios
    preciodata.unidades = int(unidades) + int(data)
    preciodata.save()

    return redirect('home')



@login_required
def editar(request, id):
    return render(request, 'editar.html', {"id": id})

@login_required
def editarArt(request, id):
    codigo_referencia = request.POST['codigo_referencia']
    nombre = request.POST['nombre']
    modelo = request.POST['modelo']
    unidades = request.POST['unidades']
    preciounidad = request.POST['preciounidad']
    precioventa = request.POST['precioventa']
    envio = request.POST['envio']




    curso = Producto.objects.get(id=id)
    if len(codigo_referencia)>0:
        curso.codigo_referencia = codigo_referencia
    if len(nombre)>0:
        curso.nombre = nombre
    if len(modelo)>0:
        curso.modelo = modelo
    if len(unidades)>0:
        curso.unidades = unidades
    if len(preciounidad)>0:
        curso.preciounidad = preciounidad
    if len(precioventa)>0:
        curso.precioventa = precioventa
    if len(envio)>0:
        curso.envio = envio
    curso.save()

    messages.success(request, '¡Datos actualizados!')

    return redirect('/')

@login_required
def eliminarArt(request, id):
    curso = Producto.objects.get(id=id)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/')

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX PLATAFORMA  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

@login_required
def plataforma(request):
    plataformadata = Producto.objects.all().values('id', 'codigo_referencia', 'nombre', 'modelo', 'etsy', 'wallapop', 'ebay', 'joom', 'amazon')
    print(plataformadata, "Data")
    return render(request, 'plataformas.html', {"Productos": plataformadata})


@login_required
def editarplataforma(request, id):
    return render(request, 'editarplataforma.html', {"id": id})
    
@login_required
def editarplataformadata(request, id):
    etsy = request.POST['etsy']
    wallapop = request.POST['wallapop']
    ebay = request.POST['ebay']
    joom = request.POST['joom']
    amazon = request.POST['amazon']


    curso = Producto.objects.get(id=id)

    if len(etsy)>0:
        curso.etsy = etsy
    if len(wallapop)>0:
        curso.wallapop = wallapop
    if len(ebay)>0:
        curso.ebay = ebay
    if len(joom)>0:
        curso.joom = joom
    if len(amazon)>0:
        curso.amazon = amazon
    curso.save()

    messages.success(request, '¡Datos actualizados!')

    return redirect('plataforma')

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX VENTAS  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

@login_required
def ventas(request):
    ventadata = Producto.objects.all().values('id','codigo_referencia', 'nombre', 'modelo')
    return render(request, 'ventas.html', {"Productosv": ventadata})


@login_required
def ventaslg(request):
    articulo = request.POST['articulo']
    ventadata = Producto.objects.all().get(codigo_referencia = articulo)
    return render(request, 'ventasdata.html', {"Productosv": ventadata})

@login_required
def ventasagg(request):
    codigo_referencia = request.POST['codigo_referencia']
    nombre = request.POST['nombre']
    modelo = request.POST['modelo']
    numserie = request.POST['numserie']
    precioventa = request.POST['precioventa']
    envio = request.POST['envio']
    cliente = request.POST['cliente']
    ventasagg = Ventas.objects.create(codigo_referencia = codigo_referencia, nombre = nombre, modelo = modelo, numserie = numserie, precioventa = precioventa, envio = envio, cliente = cliente)
    precio = Producto.objects.filter(codigo_referencia=codigo_referencia).values('unidades').values_list('unidades', flat=True)
    preciodata = Producto.objects.get(codigo_referencia=codigo_referencia)
    for precios in precio:
        data = precios
    preciodata.unidades = int(data) - int(1)
    preciodata.save()
    print(precio)
    return redirect('../ventaslist')


@login_required
def ventalist(request):
    homedata = Ventas.objects.all().values('id','codigo_referencia', 'nombre', 'modelo', 'numserie', 'precioventa', 'envio', 'cliente')
    return render(request, 'ventalist.html', {"Ventas": homedata})

@login_required
def eliminarVent(request, id):
    curso = Ventas.objects.get(id=id)
    curso.delete()

    messages.success(request, '¡Factura eliminada!')

    return redirect('../ventaslist')

@login_required
def editarVent(request, id):
    return render(request, 'editarVent.html', {"id": id})

@login_required
def editarVentdata(request, id):
    codigo_referencia = request.POST['codigo_referencia']
    nombre = request.POST['nombre']
    modelo = request.POST['modelo']
    numserie = request.POST['numserie']
    cliente = request.POST['cliente']
    precioventa = request.POST['precioventa']
    envio = request.POST['envio']




    curso = Ventas.objects.get(id=id)
    if len(codigo_referencia)>0:
        curso.codigo_referencia = codigo_referencia
    if len(nombre)>0:
        curso.nombre = nombre
    if len(modelo)>0:
        curso.modelo = modelo
    if len(numserie)>0:
        curso.numserie = numserie
    if len(precioventa)>0:
        curso.precioventa = precioventa
    if len(envio)>0:
        curso.envio = envio
    if len(cliente)>0:
        curso.cliente = cliente
    curso.save()

    messages.success(request, '¡Datos actualizados!')

    return redirect('../ventaslist')

@login_required
def perfil(request):
    user = request.user.first_name
    last_name= request.user.last_name
    imgname = Perfil.objects.filter(nombre=user).values('photo_perfil')
    data = Perfil.objects.filter(nombre=user).values('dni', 'estado', 'email', 'cargo', 'ubicacion', 'fecha_de_nacimiento')
    return render(request, 'perfil.html', {"user": user, "last_name": last_name, "imgname": imgname, "data": data})


@login_required
def fotoperfil(request):
    user = request.user.first_name
    last_name= request.user.last_name
    imgname1 = Perfil.objects.filter(nombre=user).values('photo_perfil').values_list('photo_perfil', flat=True)
    imagenperfil = request.FILES.get('imagenperfil')
    BASE_DIR = Path(__file__).resolve().parent.parent
    filedata = os.path.join(BASE_DIR, 'Productos\media\{}')
    file_path = filedata.format(imgname1[0])
    print(file_path)
    if path.exists(file_path):
        remove(file_path)
    curso = Perfil.objects.get(nombre=user)
    curso.photo_perfil = imagenperfil
    curso.save()
    imgname = Perfil.objects.filter(nombre=user).values('photo_perfil')
    data = Perfil.objects.filter(nombre=user).values('dni', 'estado', 'email', 'cargo', 'ubicacion', 'fecha_de_nacimiento')
    return render(request, 'perfil.html', {"user": user, "last_name": last_name, "imgname": imgname, "data": data})


@login_required
def añadirestado(request):
    user = request.user.first_name
    estado = request.POST['estado']
    data = Perfil.objects.get(nombre=user)
    data.estado = estado
    data.save()
    return redirect('../perfil/')






