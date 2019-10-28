from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Autor, Doctor, Noticia, Evento, Imagen


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['apellidos', 'nombres', 'email']
    list_display = ('apellidos', 'nombres', 'email',
                    'adicionado', 'modificado', 'eliminado')
    list_display_links = ('apellidos', 'nombres', 'email')
    resource_class = AutorResource


class DoctorResource(resources.ModelResource):
    class Meta:
        model = Doctor


class DocotorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['apellidos', 'nombres', 'cargo',
                     'titulo', 'directivo', 'expresidente', 'miembro', 'periodo_inicio', 'periodo_fin']
    list_display = ('apellidos', 'nombres', 'cargo', 'titulo', 'directivo', 'expresidente', 'miembro', 'periodo_inicio', 'periodo_fin',
                    'adicionado', 'modificado', 'eliminado')
    list_display_links = ('apellidos', 'nombres', 'cargo')
    resource_class = DoctorResource


class NoticiaResource(resources.ModelResource):
    class Meta:
        model = Noticia


class NoticiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'resumen',  'autor']
    list_display = ('titulo', 'resumen',  'autor', 'fecha_publicacion',
                    'adicionado', 'modificado', 'eliminado')
    list_display_links = ('titulo', 'resumen', 'autor')
    resource_class = NoticiaResource


class EventoResource(resources.ModelResource):
    class Meta:
        model = Noticia


class EventoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'resumen', 'fecha_inicio']
    list_display = ('titulo', 'resumen', 'fecha_inicio',
                    'adicionado', 'modificado', 'eliminado')
    list_display_links = ('titulo', 'resumen', 'fecha_inicio')
    resource_class = EventoResource


class ImagenResource(resources.ModelResource):
    class Meta:
        model = Imagen


class ImagenAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'titulo', 'imagen']
    list_display = ('id', 'titulo', 'imagen',
                    'adicionado', 'modificado', 'eliminado')
    list_display_links = ('id', 'titulo', 'imagen')
    resource_class = ImagenResource


# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Doctor, DocotorAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Imagen, ImagenAdmin)
