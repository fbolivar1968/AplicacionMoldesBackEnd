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
# Add 05_03_2026




# MODELO PARA HERRAMENTAR ESPECIFICO CON SUS TABLAS RELACIONADAS.

#from django.db import models

class Piso(models.Model):
    pi_IdPiso = models.AutoField(primary_key=True, db_column='pi_IdPiso')
    pi_NumeroPiso = models.CharField(max_length=10, unique=True, db_column='pi_NumeroPiso')
    pi_DescripcionPiso = models.CharField(max_length=255, null=True, blank=True, db_column='pi_DescripcionPiso')

    class Meta:
        db_table = 'PISO'
    def __str__(self): return self.pi_NumeroPiso

 

class Estanteria(models.Model):
    es_IdEstanteria = models.AutoField(primary_key=True, db_column='es_IdEstanteria')
    es_NombreEstanteria = models.CharField(max_length=50, unique=True, db_column='es_NombreEstanteria')
    piso = models.ForeignKey(Piso, on_delete=models.PROTECT, db_column='es_IdPiso', related_name='estanterias')#, default=20) # Relación con Piso, con un valor por defecto (ajustar según necesidad)

    class Meta:
        db_table = 'ESTANTERIA'
        verbose_name = 'Estantería'
        verbose_name_plural = 'Estanterías'
        ordering = ['es_NombreEstanteria']

    def __str__(self):
        return self.es_NombreEstanteria
    #def __str__(self): return self.es_NombreEstanteria #Este método define cómo se mostrará el objeto cuando se imprima o aparezca en el admin de Django



class UbicacionHerramental(models.Model):
    uh_IdUbicacionHerr = models.AutoField(primary_key=True, db_column='uh_IdUbicacionHerr')
    uh_NumeroFila = models.IntegerField(db_column='uh_NumeroFila')
    uh_NumeroColumna = models.IntegerField(db_column='uh_NumeroColumna')
    uh_NumeroPosicion = models.IntegerField(db_column='uh_NumeroPosicion')

    class Meta:
        db_table = 'UBICACIONHERRAMENTAL'
        unique_together = ('uh_NumeroFila', 'uh_NumeroColumna', 'uh_NumeroPosicion') # UQ_POSICION_DETALLE

    def __str__(self):
        return f"F:{self.uh_NumeroFila} C:{self.uh_NumeroColumna} P:{self.uh_NumeroPosicion}"


# --- TABLA DIESET ---
class DieSet(models.Model):
    di_IdDieSet = models.AutoField(primary_key=True, db_column='di_IdDieSet')
    di_CodigoDieSet = models.CharField(max_length=20, unique=True, db_column='di_CodigoDieSet')
    di_Dimensiones = models.CharField(max_length=50, null=True, blank=True, db_column='di_Dimensiones')
    # Relaciones con ubicaciones.
    piso = models.ForeignKey(Piso, on_delete=models.PROTECT, db_column='di_IdPiso')
    estanteria = models.ForeignKey(Estanteria, on_delete=models.PROTECT, db_column='di_IdEstanteria')
    ubicacion = models.ForeignKey(UbicacionHerramental, on_delete=models.PROTECT, db_column='di_IdUbicacionDieset')

    class Meta: 
        db_table = 'DIESET'
    

class HerramentalEspecifico(models.Model):
    hesp_IdHerramentalEspecifico = models.AutoField(primary_key=True, db_column='hesp_IdHerramentalEspecifico')
    hesp_CodigoHerramental = models.CharField(max_length=20, unique=True, db_column='hesp_CodigoHerramental')
    hesp_CodigoAlterno = models.CharField(max_length=15, null=True, blank=True, db_column='hesp_CodigoAlterno')
    hesp_Descripcion1 = models.TextField(null=True, blank=True, db_column='hesp_Descripcion1') # VARCHAR(MAX)
    hesp_Descripcion2 = models.TextField(null=True, blank=True, db_column='hesp_Descripcion2')
    hesp_CantHerramental = models.IntegerField(db_column='hesp_CantHerramental')
    hesp_Observacion = models.CharField(max_length=100, null=True, blank=True, db_column='hesp_Observacion')
    hesp_FechaReparacion = models.DateTimeField(null=True, blank=True, db_column='hesp_FechaReparacion')

    # Atributos técnicos (TINYINT -> PositiveSmallIntegerField, DECIMAL -> DecimalField)
    hesp_NumNariz = models.PositiveSmallIntegerField(null=True, blank=True, db_column='hesp_NumNariz')
    hesp_NumCopas = models.PositiveSmallIntegerField(null=True, blank=True, db_column='hesp_NumCopas')
    hesp_Radio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Radio')
    hesp_Altura1 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Altura1')
    hesp_Altura2 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Altura2')
    hesp_Diametro = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Diametro')
    hesp_Ancho = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Ancho')
    hesp_Profundidad = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Profundidad')
    hesp_Grado = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Grato')
    hesp_ProfunRecogida = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_ProfunRecogida')
    hesp_Largo = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Largo')

    # Dimensiones genéricas
    hesp_A = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_A')
    hesp_B = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_B')
    hesp_C = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_C')
    hesp_D = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_D')
    hesp_E = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_E')
    hesp_F = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_F')
    hesp_G = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_G')
    hesp_H = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_H')
    hesp_I = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_I')
    hesp_J = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_J')
    hesp_T = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_T')

    # RELACIONES (Foreign Keys)
    hesp_IdPiso = models.ForeignKey(Piso, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdPiso')
    hesp_IdEstanteria = models.ForeignKey(Estanteria, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdEstanteria', related_name='herramentales_especificos') # Relación con Estanteria, con un valor por defecto (ajustar según necesidad)
    hesp_IdUbicacionHerr = models.ForeignKey(UbicacionHerramental, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdUbicacionHerr')

    # IDs de otras entidades (mantener como IntegerField si no hay modelos creados aún)
    hesp_IdHerramental = models.IntegerField(null=True, blank=True,db_column='hesp_IdHerramental')
    hesp_IdTipoHerramental = models.IntegerField(null=True, blank=True, db_column='hesp_IdTipoHerramental')
    hesp_IdFamilia = models.IntegerField(null=True, blank=True,db_column='hesp_IdFamilia')
    hesp_IdEstadoHerr = models.IntegerField(null=True, blank=True, db_column='hesp_IdEstadoHerr')
    hesp_IdMaquinaPP = models.IntegerField(null=True, blank=True,db_column='hesp_IdMaquinaPP')
    hesp_IdMaquinaOpc = models.IntegerField(null=True, blank=True, db_column='hesp_IdMaquinaOpc')
    hesp_IdActividad = models.IntegerField(null=True, blank=True, db_column='hesp_IdActividad')
    hesp_IdPropiedadHerramental = models.IntegerField(null=True, blank=True, db_column='hesp_IdPropiedadHerramental')
    hesp_IdPlano = models.IntegerField(null=True, blank=True, db_column='hesp_IdPlano')
    hesp_IdManual = models.IntegerField(null=True, blank=True, db_column='hesp_IdManual')
    hesp_IdImagen = models.IntegerField(null=True, blank=True, db_column='hesp_IdImagen')
    hesp_IdDieSet = models.IntegerField(null= True, blank= True, db_column='hesp_IdDieSet')
    hesp_IdChatarrizacion = models.IntegerField(null=True, blank=True, db_column='hesp_IdChatarrizacion')
    hesp_IdOrdenProduccion = models.IntegerField(null=True, blank=True, db_column='hesp_IdOrdenProduccion')
    hesp_IdPrestamo = models.IntegerField(null=True, blank=True, db_column='hesp_IdPrestamo')

    class Meta:
        db_table = 'HERRAMENTALESPECIFICO'