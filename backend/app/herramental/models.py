from django.db import models

"""
MODELOS
--------
Todos los modelos están definidos con managed = False porque
la base de datos ya existe en SQL Server.

Django solo los usa como mapeo ORM.
"""
from django.db import models


# ==============================================================================
# SECCIÓN 1 — CATÁLOGOS SIMPLES
# Tablas maestras sin dependencias entre sí.
# =============================================================================

class TipoHerramental(models.Model):
    th_IdTipoHerramental = models.AutoField(primary_key=True, db_column='th_IdTipoHerramental')
    th_NombreTipoHerramental = models.CharField(max_length=100, db_column='th_NombreTipoHerramental')
    th_CodigoTipoHerramental = models.CharField(max_length=4, unique=True, db_column='th_CodigoTipoHerramental')

    class Meta:
        db_table = 'TIPOHERRAMENTAL'
        managed = False
        ordering = ['th_NombreTipoHerramental']


class Familia(models.Model):
    fa_IdFamilia = models.AutoField(primary_key=True, db_column='fa_IdFamilia')
    fa_CodigoFamilia = models.CharField(max_length=4, null=True, blank=True, db_column='fa_CodigoFamilia')
    fa_NombreFamilia = models.CharField(max_length=15, db_column='fa_NombreFamilia')

    class Meta:
        db_table = 'FAMILIA'
        managed = False


class EstadoHerramental(models.Model):
    eh_IdEstadoHerr = models.AutoField(primary_key=True, db_column='eh_IdEstadoHerr')
    eh_NombreEstado = models.CharField(max_length=50, db_column='eh_NombreEstadoHrr')
    #descripcion = models.TextField(null=True, blank=True, db_column='eh_DescripcionEstadoHrr')

    class Meta:
        db_table = 'ESTADOHERRAMENTAL'
        managed = False


class Herramental(models.Model):
    he_IdHerramental = models.AutoField(primary_key=True, db_column='he_IdHerramental')
    he_NombreHerramental = models.CharField(max_length=15, db_column='he_NombreHerramental')
    he_CodigoHerramental = models.CharField(max_length=4, unique=True, db_column='he_CodigoHerramental')

    class Meta:
        db_table = 'HERRAMENTAL'
        managed = False


class Maquina(models.Model):
    ma_IdMaquina = models.AutoField(primary_key=True, db_column='ma_IdMaquina')
    ma_NombreMaquina = models.CharField(max_length=100, db_column='ma_NombreMaquina')
    ma_NumMaquina = models.CharField(max_length=20, db_column='ma_NumMaquina')

    class Meta:
        db_table = 'MAQUINA'
        managed = False
        

class Actividad(models.Model):
    ac_IdActividad = models.AutoField(primary_key=True, db_column='ac_IdActividad')
    ac_NombreActividad = models.CharField(max_length=100, db_column='ac_NombreActividad')

    class Meta:
        db_table = 'ACTIVIDAD'
        managed = False


class Chatarrizacion(models.Model):
    ch_IdChatarrizacion = models.AutoField(primary_key=True, db_column='ch_IdChatarrizacion')
    ch_Descripcion = models.CharField(max_length=255, db_column='ch_Descripcion')

    class Meta:
        db_table = 'CHATARRIZACION'
        managed = False
        

class OrdenProduccion(models.Model):
    op_IdOrdenProduccion = models.AutoField(primary_key=True, db_column='op_IdOrdenProduccion')
    op_ConsecutivoOp = models.CharField(max_length=50, db_column='op_ConsecutivoOp')

    class Meta:
        db_table = 'ORDENPRODUCCION'
        managed = False
    
    def __str__(self):
        return self.op_ConsecutivoOp
    
    
class Prestamo(models.Model):
    pr_IdPrestamo = models.AutoField(primary_key=True, db_column='pr_IdPrestamo')
    pr_EstadoPrestamo = models.CharField(max_length=50, db_column='pr_EstadoPrestamo')

    class Meta:
        db_table = 'PRESTAMO'
        managed = False
        
    def __str__(self):
        return self.pr_EstadoPrestamo
    
    
# ==============================================================================
# SECCIÓN 2 — UBICACIÓN FÍSICA
# Jerarquía: Piso → Estanteria → UbicacionHerramental
# Cada nivel depende del anterior, por eso se declaran en este orden.
# ==============================================================================

class Piso(models.Model):
    pi_IdPiso = models.AutoField(primary_key=True, db_column='pi_IdPiso')
    pi_NumeroPiso = models.CharField(max_length=10, unique=True, db_column='pi_NumeroPiso')
    pi_DescripcionPiso = models.CharField(max_length=255, null=True, blank=True, db_column='pi_DescripcionPiso')

    class Meta:
        db_table = 'PISO'
        managed = False
        ordering = ['pi_NumeroPiso']
        
    def __str__(self): 
        return self.pi_NumeroPiso


class Estanteria(models.Model):
    es_IdEstanteria = models.AutoField(primary_key=True, db_column='es_IdEstanteria')
    es_NombreEstanteria = models.CharField(max_length=50, unique=True, db_column='es_NombreEstanteria')
    piso = models.ForeignKey(Piso, on_delete=models.PROTECT, db_column='es_IdPiso', related_name='estanterias')#, default=20) # Relación con Piso, con un valor por defecto (ajustar según necesidad)

    class Meta:
        db_table = 'ESTANTERIA'
        managed = False
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
        managed = False
        unique_together = ('uh_NumeroFila', 'uh_NumeroColumna', 'uh_NumeroPosicion') # UQ_POSICION_DETALLE

    def __str__(self):
        return f"F:{self.uh_NumeroFila} C:{self.uh_NumeroColumna} P:{self.uh_NumeroPosicion}"



# ==============================================================================
# SECCIÓN 3 — DIESET
# Contenedor que agrupa herramentales con ubicación propia.
# Depende de: Piso, Estanteria, UbicacionHerramental
# ==============================================================================

#----------------------------------------------------------------------------------------------------------------------------------------
# Modelos de campos relacionados con HerramentalEspecifico, para optimizar consultas con select_related (07/04/2026)
#-----------------------------------------------------------------------------------------------------------------------------------------

class DieSet(models.Model):
    di_IdDieSet = models.AutoField(primary_key=True, db_column='di_IdDieSet')
    di_CodigoDieSet = models.CharField(max_length=50, db_column='di_CodigoDieSet')
    # El DieSet tiene sus propias relaciones
    di_Dimensiones = models.CharField(max_length=255, null=True, blank=True, db_column='di_Dimensiones') # VARCHAR(MAX)
    di_IdPiso = models.ForeignKey(Piso, on_delete=models.PROTECT, db_column='di_IdPiso')
    di_IdEstanteria = models.ForeignKey(Estanteria, on_delete=models.PROTECT, db_column='di_IdEstanteria')
    di_IdUbicacionDieset = models.ForeignKey(UbicacionHerramental, on_delete=models.PROTECT, db_column='di_IdUbicacionDieset')

    class Meta:
        db_table = 'DIESET'
        managed = False



# ==============================================================================
# SECCIÓN 4 — PROPIEDADES DE MATERIAL
# Catálogos de características físicas del herramental.
# Estos tres modelos NO tienen dependencias entre sí ni con otras tablas.
# ==============================================================================

class Acero(models.Model):
    ac_IdAcero      = models.AutoField(primary_key=True, db_column='ac_IdAcero')
    ac_DescripAcero = models.CharField(max_length=50,    db_column='ac_DescripAcero')
 
    class Meta:
        db_table = 'ACERO'
        managed = False
        verbose_name = 'Acero'
        verbose_name_plural = 'Aceros'
        ordering = ['ac_DescripAcero']
 
    def __str__(self):
        return self.ac_DescripAcero
 
 
class Dureza(models.Model):
    du_IdDureza = models.AutoField(primary_key=True, db_column='du_IdDureza')
    du_ValorDureza = models.CharField(max_length=10,    db_column='du_ValorDureza')
 
    class Meta:
        db_table = 'DUREZA'
        managed = False
        verbose_name = 'Dureza'
        verbose_name_plural = 'Durezas'
        ordering = ['du_ValorDureza']
 
    def __str__(self):
        return self.du_ValorDureza
 
 
class Proveedor(models.Model):
    pr_IdProveedor = models.AutoField(primary_key=True, db_column='pr_IdProveedor')
    pr_NombreProv  = models.CharField(max_length=100,   db_column='pr_NombreProv')
 
    class Meta:
        db_table = 'PROVEEDOR'
        managed = False
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['pr_NombreProv']
 
    def __str__(self):
        return self.pr_NombreProv


class PropiedadHerramental(models.Model):
    ph_IdPropiedadHerramental = models.AutoField(primary_key=True, db_column='ph_IdPropiedadHerramental')
    ph_DescripHerra           = models.CharField(max_length=500, null=True, blank=True, db_column='ph_DescripHerra')
    ph_FechaCreacion          = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_column='ph_FechaCreacion')

    class Meta:
        db_table = 'PROPIEDADHERRAMENTAL'
        managed = False


class PropiedadHerrDureza(models.Model):
    phd_IdHerradureza = models.OneToOneField(PropiedadHerramental, on_delete=models.PROTECT, primary_key=True, db_column='phd_IdHerradureza', related_name='dureza_rel')
    phd_IdDureza      = models.ForeignKey(Dureza, on_delete=models.PROTECT, db_column='phd_IdDureza')

    class Meta:
        db_table = 'PROPIEDADHERRADUREZA'
        managed = False


class PropiedadHerrAcero(models.Model):
    pha_IdPropiedadHerracero = models.OneToOneField(PropiedadHerramental, on_delete=models.PROTECT, primary_key=True, db_column='pha_IdPropiedadHerracero', related_name='acero_rel')
    pha_IdAcero              = models.ForeignKey(Acero, on_delete=models.PROTECT, db_column='pha_IdAcero')

    class Meta:
        db_table = 'PROPIEDADHERRACERO'
        managed = False


class PropiedadHerraProveedor(models.Model):
    php_IdHerraproveedor = models.OneToOneField(PropiedadHerramental, on_delete=models.PROTECT, primary_key=True, db_column='php_IdHerraproveedor', related_name='proveedor_rel')
    php_IdProveedor      = models.ForeignKey(Proveedor, on_delete=models.PROTECT, db_column='php_IdProveedor')
    php_PrecioTotal      = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='php_PrecioTotal')

    class Meta:
        db_table = 'PROPIEDADHERRAPROVEEDOR'
        managed = False




# ==============================================================================
# SECCIÓN 5 — HERRAMENTAL ESPECÍFICO (entidad principal)
# Registro individual de cada pieza física de herramental.
# Depende de: todas las secciones anteriores.
# ==============================================================================  
#--------------------------------------------------------------------------------
# Modelos adicionales para HerramentalEspecifico, con relaciones a otras tablas para optimizar consultas y mostrar información relacionada sin necesidad de hacer múltiples consultas (07/04/2026).
#--------------------------------------------------------------------------------

class HerramentalEspecifico(models.Model):
    hesp_IdHerramentalEspecifico = models.AutoField(primary_key=True, db_column='hesp_IdHerramentalEspecifico')
    hesp_CodigoHerramental = models.CharField(max_length=20, unique=True, db_column='hesp_CodigoHerramental')
    hesp_CodigoAlterno = models.CharField(max_length=15, null=True, blank=True, db_column='hesp_CodigoAlterno')
    hesp_Descripcion1 = models.TextField(null=True, blank=True, db_column='hesp_Descripcion1') # VARCHAR(MAX)
    hesp_Descripcion2 = models.TextField(null=True, blank=True, db_column='hesp_Descripcion2')
    hesp_CantHerramental = models.IntegerField(db_column='hesp_CantHerramental')
    hesp_Observacion = models.CharField(max_length=100, null=True, blank=True, db_column='hesp_Observacion')
    hesp_FechaReparacion = models.DateTimeField(null=True, blank=True, db_column='hesp_FechaReparacion')
    hesp_Criticidad = models.CharField(max_length=20, null=True, blank=True, db_column='hesp_Criticidad')
    # Atributos técnicos (TINYINT -> PositiveSmallIntegerField, DECIMAL -> DecimalField)
    hesp_NumNariz = models.PositiveSmallIntegerField(null=True, blank=True, db_column='hesp_NumNariz')
    hesp_NumCopas = models.PositiveSmallIntegerField(null=True, blank=True, db_column='hesp_NumCopas')
    hesp_Radio = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Radio')
    hesp_Altura1 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Altura1')
    hesp_Altura2 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Altura2')
    hesp_Diametro = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Diametro')
    hesp_Ancho = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Ancho')
    hesp_Profundidad = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Profundidad')
    hesp_Grado = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Grado')
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
    hesp_L = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_L')
    hesp_P = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_P')
    hesp_Q = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_Q')
    hesp_T = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, db_column='hesp_T')
    # RELACIONES (Foreign Keys)
    hesp_IdPiso = models.ForeignKey(Piso, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdPiso')
    hesp_IdEstanteria = models.ForeignKey(Estanteria, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdEstanteria', related_name='herramentales_especificos') # Relación con Estanteria, con un valor por defecto (ajustar según necesidad)
    hesp_IdUbicacionHerr = models.ForeignKey(UbicacionHerramental, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdUbicacionHerr')
    hesp_IdHerramental = models.ForeignKey(Herramental, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdHerramental')    
    hesp_IdFamilia = models.ForeignKey(Familia, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdFamilia')
    hesp_IdTipoHerramental = models.ForeignKey(TipoHerramental, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdTipoHerramental')
    hesp_IdEstadoHerr = models.ForeignKey(EstadoHerramental, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdEstadoHerr')
    hesp_IdMaquinaPP = models.ForeignKey('Maquina', on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdMaquinaPP', related_name='herramentales_principales')
    hesp_IdMaquinaOpc = models.ForeignKey('Maquina', on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdMaquinaOpc', related_name='herramentales_opcionales')
    hesp_IdActividad = models.ForeignKey('Actividad', on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdActividad')
    hesp_IdDieSet = models.ForeignKey(DieSet, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdDieSet')
    hesp_IdChatarrizacion = models.ForeignKey(Chatarrizacion, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdChatarrizacion')
    hesp_IdOrdenProduccion = models.ForeignKey(OrdenProduccion, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdOrdenProduccion')
    hesp_IdPrestamo = models.ForeignKey(Prestamo, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdPrestamo')
    hesp_IdPropiedadHerramental = models.ForeignKey(PropiedadHerramental, on_delete=models.PROTECT, null=True, blank=True, db_column='hesp_IdPropiedadHerramental')
    hesp_IdPlano = models.IntegerField(null=True, blank=True, db_column='hesp_IdPlano')
    hesp_IdManual = models.IntegerField(null=True, blank=True, db_column='hesp_IdManual')
    hesp_IdImagen = models.IntegerField(null=True, blank=True, db_column='hesp_IdImagen')

    class Meta:
        db_table = 'HERRAMENTALESPECIFICO'
        managed = False
        
