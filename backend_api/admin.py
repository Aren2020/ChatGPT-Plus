from django.contrib import admin
from .models import Section,ApiStatus

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id',]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ApiStatus)
class ApiStatusAdmin(admin.ModelAdmin):
    list_display = ['api','starttime','trycount','status','disable']

