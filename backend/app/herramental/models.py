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


#------------------------------------------------------------------------------------------
# Add 27_01_2026

class estadoHerramental(models.Model):
    id = models.AutoField(primary_key=True, db_column='eh_IdEstadoHerr')
    nombre = models.CharField(max_length=20, db_column='eh_NombreEstadoHrr')
    descripcion = models.TextField(null=True, blank=True, db_column='eh_DescripcionEstadoHrr')

    class Meta:
        db_table = 'ESTADOHERRAMENTAL'
        managed = False

#------------------------------------------------------------------------------------------
# Add 12_02_2026

from django.db import models

class HerramentalEspecifico(models.Model):
    # Identificador y Códigos
    hesp_IdHerramentalEspecifico = models.AutoField(primary_key=True, db_column='hesp_IdHerramentalEspecifico')
    hesp_CodigoHerramental = models.CharField(max_length=20, unique=True, db_column='hesp_CodigoHerramental')
    hesp_CodigoAlterno = models.CharField(max_length=15, null=True, blank=True, db_column='hesp_CodigoAlterno')
    
    # Descripciones largas (VARCHAR MAX)
    hesp_Descripcion1 = models.TextField(null=True, blank=True, db_column='hesp_Descripcion1')
    hesp_Descripcion2 = models.TextField(null=True, blank=True, db_column='hesp_Descripcion2')
    
    # Información General
    hesp_CantPieza = models.IntegerField(db_column='hesp_CantPieza')
    hesp_Observacion = models.CharField(max_length=100, null=True, blank=True, db_column='hesp_Observacion')
    hesp_FechaReparacion = models.DateTimeField(null=True, blank=True, db_column='hesp_FechaReparacion')

    # Atributos Técnicos (TINYINT -> PositiveSmallIntegerField)
    hesp_NumNariz = models.PositiveSmallIntegerField(null=True, blank=True, db_column='hesp_NumNariz')
    hesp_NumCopas = models.PositiveSmallIntegerField(null=True, blank=True, db_column='hesp_NumCopas')
    
    # Medidas y Dimensiones (DECIMAL 10,4)
    hesp_Radio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Radio')
    hesp_Altura1 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Altura1')
    hesp_Altura2 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Altura2')
    hesp_Diametro = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Diametro')
    hesp_Ancho = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Ancho')
    hesp_Profundidad = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Profundidad')
    hesp_Grado = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Grato')
    hesp_ProfunRecogida = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_ProfunRecogida')
    hesp_Largo = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Largo')

    # Dimensiones Genéricas
    hesp_A = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_A')
    hesp_B = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_B')
    hesp_C = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_C')
    hesp_D = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_D')

    """ 
    # --- RELACIONES PRINCIPALES ---
    estado = models.ForeignKey('EstadoHerramental', on_delete=models.PROTECT, db_column='hesp_IdEstadoHerr', related_name='herramentales_esp')
    piso = models.ForeignKey('Piso', on_delete=models.PROTECT, db_column='hesp_IdPiso', related_name='herramentales_piso')
    estanteria = models.ForeignKey('Estanteria', on_delete=models.PROTECT, db_column='hesp_IdEstanteria', related_name='herramentales_est')
    actividad = models.ForeignKey('Actividad', on_delete=models.SET_NULL, null=True, blank=True, db_column='hesp_IdActividad')

    # --- OTRAS RELACIONES (Basadas en nombres de ID) ---
    # Nota: Estos modelos deben existir o crearse con estos nombres
    hesp_IdHerramental = models.IntegerField(db_column='hesp_IdHerramental') # Podría ser otra FK
    hesp_IdTipoHerramental = models.IntegerField(db_column='hesp_IdTipoHerramental')
    hesp_IdFamilia = models.IntegerField(db_column='hesp_IdFamilia')
    hesp_IdMaquinaPP = models.IntegerField(db_column='hesp_IdMaquinaPP')
    hesp_IdUbicacionHerr = models.IntegerField(db_column='hesp_IdUbicacionHerr')
    hesp_IdDieSet = models.IntegerField(db_column='hesp_IdDieSet')
"""
    class Meta:
        db_table = 'HERRAMENTALESPECIFICO'

    def __str__(self):
        return f"{self.hesp_CodigoHerramental} - {self.hesp_Descripcion1[:30]}"