from django.db import models

# Create your models here.

class Membresia(models.Model):
    MODALIDAD_CHOICES=(
        ('D','Diario'),
        ('M','Mensual'),
        ('S','Semestral'),
        ('A','Anual'),
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

    #def __str__(self):
     #   return '%s %s'%(self.nombre,self.apellido)

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
    fecha_fin = models.DateField()
    estado = models.CharField("Estado del contrato",max_length=1,choices=ESTADO_CHOICES,default=ACTIVO)

    def __str__(self):
        return '%s %s'%(self.coworker,self.membresia)

    class Meta:
        order_with_respect_to = 'coworker'
        verbose_name_plural="Planes - Coworker's"