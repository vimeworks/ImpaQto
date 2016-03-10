from django.db import models
from django.template.defaultfilters import default


# Create your models here.

class Membresia(models.Model):
    MODALIDAD_CHOICES=(
        #('D','Diario'),
        ('M','Mensual'),
        #('S','Semestral'),
        #('A','Anual'),
    )
    STATE_CHOICES=(
        ('A','Activo'),
        ('I','Inactivo'),
    )
    nombre = models.TextField("Nombre de la membresía")
    uso_espacio = models.IntegerField("Uso de Espacio")
    modalidad = models.CharField("Modalidad de la membresía",max_length=1,choices=MODALIDAD_CHOICES)
    estado = models.CharField("Estado de la membresía",max_length=1,choices=STATE_CHOICES)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
    
class Coworker(models.Model):
    nombre = models.CharField("Nombre del Coworker",max_length=250)
    apellido = models.CharField("Apellido del Coworker",max_length=250)
    mail= models.EmailField("Correo Electrónico del Coworker",unique=True,null=False,blank=True)
    username = models.CharField("Usuario",max_length=16,null=False,blank=True)

    def __str__(self):
        return '%s %s'%(self.nombre,self.apellido)

    def mail_default(self):
        return {"mail":"to1@ejemplo.com"}

    class Meta:
        ordering = ["apellido"]
        verbose_name_plural="Coworker's"
        
class Contrato(models.Model):
    ACTIVO='A'
    INACTIVO='I'

    ESTADO_CHOICES=(
        (ACTIVO,'Activo'),
        (INACTIVO,'Inactivo'),
    )
    coworker = models.ForeignKey(Coworker,verbose_name="Nombre del Coworkers")
    membresia = models.ForeignKey(Membresia,verbose_name="Nombre de la membresía")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True,blank=True)
    estado = models.CharField("Estado del contrato",max_length=1,choices=ESTADO_CHOICES,default=ACTIVO)
    minutos_mes = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    def __str__(self):
        return '%s %s'%(self.coworker,self.membresia)

    class Meta:
        order_with_respect_to = 'coworker'
        verbose_name_plural="Planes - Coworker's"


class ControlConsumo(models.Model):
    mes = models.IntegerField()
    anio = models.IntegerField("Año")
    control_minutos = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    contrato = models.ForeignKey(Contrato,verbose_name="Contrato a elegir")
    
    def __str__(self):
        return 'En %s del % '%(self.mes,self.anio)
    class Meta:
        ordering = ["anio"]
        verbose_name_plural = "Resumen del Consumo"


class Consumo(models.Model):
    ENTRADA ='E'
    SALIDA = 'S'
    REGISTRO_CHOICES=(
                      (ENTRADA,'Entrada'),
                      (SALIDA,'Salida'),
    )
    estado_registro = models.CharField("Registro de ",max_length=1,choices = REGISTRO_CHOICES,default=ENTRADA)
    fecha_entrada = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_salida = models.DateTimeField(null=True,blank=True)
    minutos = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    control_consumo = models.ForeignKey(ControlConsumo,verbose_name="Control Consumo",null=False,blank=False)
    
    def __str__(self):
        return '%s '%(self.contrato)
    class Meta:
        ordering = ["fecha_entrada"]
        verbose_name_plural = "Asistencia"

