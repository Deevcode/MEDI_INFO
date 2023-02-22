from django.contrib import admin
from .models import TipoFarmaco , Laboratorio, MarcaMedicamento, ViaAdminstracion, Medicamento
# Register your models here.

#class MedicamentoAdmin(admin.ModelAdmin):
#    list_display = ["nombre", "medida", "cantidad", "tipoFarmaco","laboratorio","marca","viaAdmin","fecha_vencimento"]
#    search_fields = ["nombre"]
#    list_editable = ["medida", "cantidad"]


admin.site.register(TipoFarmaco)
admin.site.register(Laboratorio)
admin.site.register(MarcaMedicamento)
admin.site.register(ViaAdminstracion)
admin.site.register(Medicamento)