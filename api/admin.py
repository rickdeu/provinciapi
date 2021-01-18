from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.admin import ExportActionMixin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field 
from import_export.admin import ExportActionMixin


class MunicipioInlne(admin.TabularInline):
    model = Municipio
    extra = 1
 

class ProvinciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [
        ('Provincias',               {'fields': ['province']}), ]
    inlines = [MunicipioInlne]
    list_display=['province']
    list_filter = ['province']
    search_fields = ['province']


class BairroInlne(admin.TabularInline):
    model = Bairro
    extra = 1
 

class MunicipioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [
        ('Provincias',               {'fields': ['municipe','id_province']}), ]
    inlines = [BairroInlne]
    list_display=('municipe','id_province')
    list_display_links=('municipe','id_province')

    list_filter = ['id_province','municipe']
    search_fields = ['municipe','id_province__province']
    autocomplete_fields = ['id_province']


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
#admin.site.register(Bairro)