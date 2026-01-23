from django.db import models

"""
MODELOS
--------
Todos los modelos están definidos con managed = False porque
la base de datos ya existe en SQL Server.

Django solo los usa como mapeo ORM.
"""
from django.db import models

class TipoHerramental(models.Model):
    id = models.AutoField(primary_key=True, db_column='th_IdTipoHerramental')
    nombre = models.CharField(max_length=15, db_column='th_NombreTipoHerramental')
    codigo = models.CharField(max_length=4, unique=True, db_column='th_CodigoTipoHerramental')

    class Meta:
        db_table = 'TIPOHERRAMENTAL' # Nombre exacto de la tabla en la base de datos.
        managed = False # (False)Indica que Django no debe gestionar la tabla.


class Herramental(models.Model):
    id = models.AutoField(primary_key=True, db_column='he_IdHerramental')
    nombre = models.CharField(max_length=15, db_column='he_NombreHerramental')
    codigo = models.CharField(max_length=4, unique=True, db_column='he_CodigoHerramental')

    class Meta:
        db_table = 'HERRAMENTAL'
        managed = False


class Familia(models.Model):
    id = models.AutoField(primary_key=True, db_column='fa_IdFamilia')
    codigo = models.CharField(max_length=4, null=True, blank=True, db_column='fa_CodigoFamilia')
    nombre = models.CharField(max_length=15, db_column='fa_NombreFamilia')

    class Meta:
        db_table = 'FAMILIA'
        managed = False
