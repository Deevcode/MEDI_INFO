from django.db import models

#TABLA TIPO DE FARMACO
class TipoFarmaco(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#TABLA LABORATORIO
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#MARCA DEL MEDICAMENTO
class MarcaMedicamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#TABLA DE ADMINISTRACION MEDICAMENTO
class ViaAdminstracion(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre

#TABLA DE MEDICAMENTO
class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.CharField(max_length=10)
    cantidad = models.IntegerField
    tipoFarmaco = models.ForeignKey(TipoFarmaco, on_delete=models.PROTECT)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    marca = models.ForeignKey(MarcaMedicamento, on_delete=models.PROTECT)
    viaAdmin = models.ForeignKey(ViaAdminstracion, on_delete=models.PROTECT)
    fecha_vencimento = models.DateField()

    def __str__(self):
        return self.nombre


