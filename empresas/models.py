from django.db import models

# Create your models here.
class Empresa(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('SUSPENSION TEMPORAL', 'Suspensión Temporal'),
        ('CANCELADO', 'Cancelado'),
    ]
    nombre = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20)
    dv = models.CharField(max_length=2)
    contabilidad = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ACTIVO')
    fdesde = models.DateField(null=True, blank=True,verbose_name='Fecha de inicio')
    fhasta = models.DateField(null=True, blank=True,verbose_name='Fecha de finalización')

    def __str__(self):
        return f"{self.nombre} ({self.ruc}-{self.dv})"