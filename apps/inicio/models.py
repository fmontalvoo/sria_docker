from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='autores', blank=True, null=True)
    apellidos = models.CharField(
        'Apellidos', max_length=255, null=False, blank=False)
    nombres = models.CharField(
        'Nombres', max_length=255, null=False, blank=False)
    biografia = models.TextField(
        'Biografia', max_length=250, blank=True, null=True)
    genero = models.CharField('Genero', max_length=1, choices=(
        ('M', 'Masculino'), ('F', 'Femenino')))
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', null=False, blank=False)
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0} {1}'.format(self.apellidos, self.nombres)


class Doctor(models.Model):
    now = datetime.now()
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='doctores', blank=True, null=True)
    apellidos = models.CharField(
        'Apellidos', max_length=255, null=False, blank=False)
    nombres = models.CharField(
        'Nombres', max_length=255, null=False, blank=False)
    cargo = models.CharField(
        'Cargo', max_length=100, null=False, blank=False)
    titulo = models.CharField(
        'Titulo', max_length=100, null=False, blank=False)
    biografia = models.TextField(
        'Biografia', max_length=500, blank=True, null=True)
    directivo = models.BooleanField('Es parte del Directorio', default=False)
    expresidente = models.BooleanField('Es Expresidente', default=False)
    miembro = models.BooleanField('Es Miembro', default=False)
    periodo_inicio = models.IntegerField('Inicio de Periodo', default=now.year)
    periodo_fin = models.IntegerField('Fin de Periodo', default=now.year)
    email = models.EmailField('Correo Electrónico', null=False, blank=False)
    web = models.URLField('Web Personal', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'
        ordering = ['-periodo_fin']

    def __str__(self):
        return 'Dr. {0} {1}'.format(self.nombres, self.apellidos)


class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Titulo', max_length=100, blank=False, null=False
    )
    imagen = models.ImageField(upload_to='noticias')
    fecha_publicacion = models.DateField('Fecha Publicación')
    resumen = models.TextField(
        'Resumen', max_length=250, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    contenido = RichTextField('Contenido')
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return '{0}'.format(self.titulo)


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Titulo', max_length=100, blank=False, null=False
    )
    imagen = models.ImageField(upload_to='eventos')
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_fin = models.DateField('Fecha de Fin')
    resumen = models.TextField(
        'Resumen', max_length=250, blank=True, null=True)
    contenido = RichTextField('Contenido')
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return '{0}'.format(self.titulo)


class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes')
    titulo = models.CharField(
        'Titulo', max_length=100, blank=False, null=False
    )
    adicionado = models.DateField('Adicionado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    eliminado = models.BooleanField('Eliminado', default=False)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

        def __str__(self):
            return '{0}'.format(self.titulo)
