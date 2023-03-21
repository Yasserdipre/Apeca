from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo_referencia = models.CharField(max_length = 40, verbose_name= 'codigo_referencia', unique=True)
    nombre = models.CharField(max_length = 60, verbose_name= 'Nombres')
    modelo = models.CharField(max_length = 40, verbose_name= 'Modelo')
    unidades = models.CharField(max_length = 60, verbose_name= 'unidades')
    preciounidad = models.FloatField(verbose_name= 'Precio_Unidad')
    precioventa = models.FloatField(verbose_name= 'Precio_Venta')
    envio = models.FloatField(verbose_name= 'Envio')
    etsy = models.FloatField(verbose_name= 'Etsy', null=True)
    wallapop = models.FloatField(verbose_name= 'Wallapop', null=True)
    ebay = models.FloatField(verbose_name= 'Ebay', null=True)
    joom = models.FloatField(verbose_name= 'Joom', null=True)
    amazon = models.FloatField(verbose_name= 'Amazon', null=True)


    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    codigo_clientes = models.CharField(max_length = 40, verbose_name= 'codigo_clientes', unique=True)
    nombre = models.CharField(max_length = 60, verbose_name= 'Nombres')
    apellido = models.CharField(max_length = 40, verbose_name= 'Apellido')
    direccion = models.CharField(max_length = 60, verbose_name= 'Direccion')
    plataforma = models.CharField(max_length = 60, verbose_name= 'Plataforma')

class Ventas(models.Model):
    codigo_referencia = models.CharField(max_length = 40, verbose_name= 'codigo_referencia')
    nombre = models.CharField(max_length = 60, verbose_name= 'Nombres')
    modelo = models.CharField(max_length = 40, verbose_name= 'Modelo')
    numserie = models.CharField(max_length = 60, verbose_name= 'numserie', unique=True)
    precioventa = models.FloatField(verbose_name= 'precioventa')
    envio = models.FloatField(verbose_name= 'envio')
    cliente = models.CharField(max_length = 60, verbose_name= 'cliente')


class Perfil(models.Model):
    dni = models.CharField(max_length = 15, verbose_name= 'dni', unique=True)
    nombre = models.CharField(max_length = 60, verbose_name= 'nombre')
    apellido = models.CharField(max_length = 40, verbose_name= 'apellido')
    estado = models.CharField(max_length = 500, verbose_name= 'estado')
    email = models.CharField(max_length = 60, verbose_name= 'email')
    cargo = models.CharField(max_length = 60, verbose_name= 'cargo')
    ubicacion = models.CharField(max_length = 60, verbose_name= 'ubicacion')
    fecha_de_nacimiento = models.DateField(verbose_name= 'fecha_de_nacimiento')
    photo_perfil = models.ImageField(upload_to="photo_perfil", null=True)
    photo_fondo = models.ImageField(upload_to="photo_fondo", null=True)
    
    def __str__(self):
        return self.nombre