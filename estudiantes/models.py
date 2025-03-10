from django.db import models

# Create your models here.

class estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=255, verbose_name='apellidos')
    nombres = models.CharField(max_length=255, verbose_name='nombres')
    documento = models.IntegerField(verbose_name='documento')
    curso = models.IntegerField(verbose_name='curso', null=True)
    linea = models.CharField(max_length=255, verbose_name='linea', null=True)
    foto = models.ImageField(upload_to='fotos/', null=True, verbose_name='foto')
    qr = models.ImageField(upload_to='qrs/', null=True, verbose_name='qr')
    
    def __str__(self):
        fila = "Nombre: " + self.apellidos + " " + self.nombres + " Linea: " + self.linea + " Curso: " + str(self.curso)
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        self.qr.storage.delete(self.qr.name)
        super().delete()

class qrScan(models.Model):
    id = models.AutoField(primary_key=True)
    qr_value = models.IntegerField()

    def __str__(self):
        return self.qr_value