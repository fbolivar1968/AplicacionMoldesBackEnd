#from django.db import models

# Create your models here.
from django.db import models


class EstadoMaquina(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='ea_IdEstadoMaquina'
    )
    nombre = models.CharField(
        max_length=30,
        db_column='ea_NombreEstMaquina'
    )

    class Meta:
        db_table = 'ESTADOMAQUINA'
        managed = False


class TipoMaquina(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='tm_IdTipoMaquina'
    )
    nombre = models.CharField(
        max_length=30,
        db_column='tm_NombreTipoMaquina'
    )
    descripcion = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        db_column='tm_Descripcion'
    )

    class Meta:
        db_table = 'TIPOMAQUINA'
        managed = False


class Maquina(models.Model):
    """
    Modelo MAQUINA

    Representa una máquina física de planta.
    Mapeado 1:1 contra SQL Server.
    """

    id = models.AutoField(
        primary_key=True,
        db_column='ma_IdMaquina'
    )

    numero = models.IntegerField(
        db_column='ma_NumMaquina'
    )

    nombre = models.CharField(
        max_length=30,
        db_column='ma_NombreMaquina'
    )

    anio_instalacion = models.DateField(
        null=True,
        blank=True,
        db_column='ma_AnioInstalacion'
    )

    marca = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        db_column='ma_Marca'
    )

    capacidad = models.FloatField(
        null=True,
        blank=True,
        db_column='ma_CapMaquina'
    )

    codigo = models.CharField(
        max_length=20,
        unique=True,
        db_column='ma_CodigoMaquina'
    )

    descripcion = models.TextField(
        null=True,
        blank=True,
        db_column='ma_DescMaquina'
    )

    estado = models.ForeignKey(
        EstadoMaquina,
        on_delete=models.PROTECT,
        db_column='ma_IdEstadoMaquina',
        related_name='maquinas'
    )

    tipo = models.ForeignKey(
        TipoMaquina,
        on_delete=models.PROTECT,
        db_column='ma_IdTipoMaquina',
        related_name='maquinas'
    )

    class Meta:
        db_table = 'MAQUINA'
        managed = False

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"




# Tabla actividad --------------------------------------------------

class Actividad(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='ac_IdActividad'
    )

    nombre = models.CharField(
        max_length=30,
        db_column='ac_NombreActividad'
    )

    fecha_creacion = models.DateTimeField(
        db_column='ac_FechaCreacionActivdad'
    )

    descripcion = models.CharField(
        max_length=500,
        db_column='ac_DescripcionActividad'
    )

    usuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.PROTECT,
        db_column='ac_IdUsuario', 
        related_name='actividades'
    )

    class Meta:
        db_table = 'ACTIVIDAD'
        managed = False
        #ordering = ['-ac_FechaCreacionActivdad']

    #def __str__(self):
     #   return self.nombre