from django.contrib import admin
from .models import TipoFarmaco , Laboratorio, MarcaMedicamento, ViaAdminstracion, Medicamento
# Register your models here.

admin.site.register(TipoFarmaco)
admin.site.register(Laboratorio)
admin.site.register(MarcaMedicamento)
admin.site.register(ViaAdminstracion)
admin.site.register(Medicamento)