from django.contrib import admin
from .models import Fotografia

# Register your models here.
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    admin.site.register(Fotografia)