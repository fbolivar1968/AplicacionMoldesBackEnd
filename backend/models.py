# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividad(models.Model):
    ac_idactividad = models.AutoField(db_column='ac_IdActividad', primary_key=True)  # Field name made lowercase.
    ac_nombreactividad = models.CharField(db_column='ac_NombreActividad', max_length=30)  # Field name made lowercase.
    ac_fechacreacionactivdad = models.DateTimeField(db_column='ac_FechaCreacionActivdad')  # Field name made lowercase.
    ac_descripcionactividad = models.CharField(db_column='ac_DescripcionActividad', max_length=500)  # Field name made lowercase.
    ac_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ac_IdUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACTIVIDAD'


class Alertaactividad(models.Model):
    aa_idalertaactividad = models.AutoField(db_column='aa_IdAlertaActividad', primary_key=True)  # Field name made lowercase.
    aa_fechacreacionalerta = models.DateTimeField(db_column='aa_FechaCreacionAlerta')  # Field name made lowercase.
    aa_descripcion = models.CharField(db_column='aa_Descripcion', max_length=500)  # Field name made lowercase.
    aa_idactividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='aa_IdActividad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERTAACTIVIDAD'


class Alertadesviacion(models.Model):
    ad_idalertadesviacion = models.AutoField(db_column='ad_IdAlertaDesviacion', primary_key=True)  # Field name made lowercase.
    ad_descripcionalertadesv = models.CharField(db_column='ad_DescripcionAlertaDesv', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ad_iddesviacion = models.ForeignKey('Desviacion', models.DO_NOTHING, db_column='ad_IdDesviacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALERTADESVIACION'


class Cargo(models.Model):
    ca_idcargo = models.AutoField(db_column='ca_IdCargo', primary_key=True)  # Field name made lowercase.
    ca_nombrecargo = models.CharField(db_column='ca_NombreCargo', unique=True, max_length=50)  # Field name made lowercase.
    ca_area = models.CharField(db_column='ca_Area', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARGO'


class Chatarrizacion(models.Model):
    ch_idchatarrizacion = models.AutoField(db_column='ch_IdChatarrizacion', primary_key=True)  # Field name made lowercase.
    ch_pesoneto = models.FloatField(db_column='ch_PesoNeto')  # Field name made lowercase.
    ch_precioventa = models.DecimalField(db_column='ch_PrecioVenta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ch_fechachatarrizacion = models.DateTimeField(db_column='ch_FechaChatarrizacion')  # Field name made lowercase.
    ch_descripcion = models.CharField(db_column='ch_Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHATARRIZACION'


class Desviacion(models.Model):
    de_iddesviacion = models.AutoField(db_column='de_IdDesviacion', primary_key=True)  # Field name made lowercase.
    de_descripciondesviacion = models.CharField(db_column='de_DescripcionDesviacion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    de_idultproducto = models.ForeignKey('Ultimoproducto', models.DO_NOTHING, db_column='de_IdUltProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DESVIACION'


class Dieset(models.Model):
    di_iddieset = models.AutoField(db_column='di_IdDieSet', primary_key=True)  # Field name made lowercase.
    di_codigodieset = models.CharField(db_column='di_CodigoDieSet', unique=True, max_length=20)  # Field name made lowercase.
    di_dimensiones = models.CharField(db_column='di_Dimensiones', max_length=50, blank=True, null=True)  # Field name made lowercase.
    di_idpiso = models.ForeignKey('Piso', models.DO_NOTHING, db_column='di_IdPiso')  # Field name made lowercase.
    di_idestanteria = models.ForeignKey('Estanteria', models.DO_NOTHING, db_column='di_IdEstanteria')  # Field name made lowercase.
    di_idubicaciondieset = models.ForeignKey('Ubicacionherramental', models.DO_NOTHING, db_column='di_IdUbicacionDieset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIESET'


class Estadoherramental(models.Model):
    eh_idestadoherr = models.AutoField(db_column='eh_IdEstadoHerr', primary_key=True)  # Field name made lowercase.
    eh_nombreestadohrr = models.CharField(db_column='eh_NombreEstadoHrr', max_length=20)  # Field name made lowercase.
    eh_descripcionestadohrr = models.TextField(db_column='eh_DescripcionEstadoHrr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADOHERRAMENTAL'


class Estadoherramentalactividad(models.Model):
    pk = models.CompositePrimaryKey('ema_IdEstadoHerr', 'ema_IdActividad')
    ema_idestadoherr = models.ForeignKey(Estadoherramental, models.DO_NOTHING, db_column='ema_IdEstadoHerr')  # Field name made lowercase.
    ema_idactividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ema_IdActividad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADOHERRAMENTALACTIVIDAD'


class Estadomaquina(models.Model):
    ea_idestadomaquina = models.AutoField(db_column='ea_IdEstadoMaquina', primary_key=True)  # Field name made lowercase.
    ea_nombreestmaquina = models.CharField(db_column='ea_NombreEstMaquina', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADOMAQUINA'


class Estanteria(models.Model):
    es_idestanteria = models.AutoField(db_column='es_IdEstanteria', primary_key=True)  # Field name made lowercase.
    es_nombreestanteria = models.CharField(db_column='es_NombreEstanteria', max_length=50)  # Field name made lowercase.
    es_idpiso = models.ForeignKey('Piso', models.DO_NOTHING, db_column='es_IdPiso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTANTERIA'


class Familia(models.Model):
    fa_idfamilia = models.AutoField(db_column='fa_IdFamilia', primary_key=True)  # Field name made lowercase.
    fa_codigofamilia = models.CharField(db_column='fa_CodigoFamilia', unique=True, max_length=4, blank=True, null=True)  # Field name made lowercase.
    fa_nombrefamilia = models.CharField(db_column='fa_NombreFamilia', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FAMILIA'


class Gestionusuarioherramental(models.Model):
    pk = models.CompositePrimaryKey('gum_IdHerramental', 'gum_IdUsuario')
    gum_idherramental = models.ForeignKey('Herramental', models.DO_NOTHING, db_column='gum_IdHerramental')  # Field name made lowercase.
    gum_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='gum_IdUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GESTIONUSUARIOHERRAMENTAL'


class Herramental(models.Model):
    he_idherramental = models.AutoField(db_column='he_IdHerramental', primary_key=True)  # Field name made lowercase.
    he_nombreherramental = models.CharField(db_column='he_NombreHerramental', max_length=15)  # Field name made lowercase.
    he_codigoherramental = models.CharField(db_column='he_CodigoHerramental', unique=True, max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HERRAMENTAL'


class Herramentalespecifico(models.Model):
    hesp_idherramentalespecifico = models.AutoField(db_column='hesp_IdHerramentalEspecifico', primary_key=True)  # Field name made lowercase.
    hesp_codigoherramental = models.CharField(db_column='hesp_CodigoHerramental', unique=True, max_length=20)  # Field name made lowercase.
    hesp_codigoalterno = models.CharField(db_column='hesp_CodigoAlterno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    hesp_descripcion1 = models.TextField(db_column='hesp_Descripcion1', blank=True, null=True)  # Field name made lowercase.
    hesp_descripcion2 = models.TextField(db_column='hesp_Descripcion2', blank=True, null=True)  # Field name made lowercase.
    hesp_cantpieza = models.IntegerField(db_column='hesp_CantPieza')  # Field name made lowercase.
    hesp_observacion = models.CharField(db_column='hesp_Observacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hesp_fechareparacion = models.DateTimeField(db_column='hesp_FechaReparacion', blank=True, null=True)  # Field name made lowercase.
    hesp_numnariz = models.SmallIntegerField(db_column='hesp_NumNariz', blank=True, null=True)  # Field name made lowercase.
    hesp_numcopas = models.SmallIntegerField(db_column='hesp_NumCopas', blank=True, null=True)  # Field name made lowercase.
    hesp_radio = models.DecimalField(db_column='hesp_Radio', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_altura1 = models.DecimalField(db_column='hesp_Altura1', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_altura2 = models.DecimalField(db_column='hesp_Altura2', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_diametro = models.DecimalField(db_column='hesp_Diametro', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_ancho = models.DecimalField(db_column='hesp_Ancho', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_profundidad = models.DecimalField(db_column='hesp_Profundidad', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_grato = models.DecimalField(db_column='hesp_Grato', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_profunrecogida = models.DecimalField(db_column='hesp_ProfunRecogida', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_largo = models.DecimalField(db_column='hesp_Largo', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_a = models.DecimalField(db_column='hesp_A', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_b = models.DecimalField(db_column='hesp_B', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_c = models.DecimalField(db_column='hesp_C', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_d = models.DecimalField(db_column='hesp_D', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hesp_idherramental = models.ForeignKey(Herramental, models.DO_NOTHING, db_column='hesp_IdHerramental')  # Field name made lowercase.
    hesp_idtipoherramental = models.ForeignKey('Tipoherramental', models.DO_NOTHING, db_column='hesp_IdTipoHerramental')  # Field name made lowercase.
    hesp_idfamilia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='hesp_IdFamilia')  # Field name made lowercase.
    hesp_idestadoherr = models.ForeignKey(Estadoherramental, models.DO_NOTHING, db_column='hesp_IdEstadoHerr')  # Field name made lowercase.
    hesp_idmaquinapp = models.ForeignKey('Maquina', models.DO_NOTHING, db_column='hesp_IdMaquinaPP')  # Field name made lowercase.
    hesp_idmaquinaopc = models.ForeignKey('Maquina', models.DO_NOTHING, db_column='hesp_IdMaquinaOpc', related_name='herramentalespecifico_hesp_idmaquinaopc_set', blank=True, null=True)  # Field name made lowercase.
    hesp_idactividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='hesp_IdActividad', blank=True, null=True)  # Field name made lowercase.
    hesp_idpropiedadherramental = models.ForeignKey('Propiedadherramental', models.DO_NOTHING, db_column='hesp_IdPropiedadHerramental', blank=True, null=True)  # Field name made lowercase.
    hesp_idplano = models.ForeignKey('Plano', models.DO_NOTHING, db_column='hesp_IdPlano', blank=True, null=True)  # Field name made lowercase.
    hesp_idmanual = models.ForeignKey('Manual', models.DO_NOTHING, db_column='hesp_IdManual', blank=True, null=True)  # Field name made lowercase.
    hesp_idimagen = models.ForeignKey('Imagen', models.DO_NOTHING, db_column='hesp_IdImagen', blank=True, null=True)  # Field name made lowercase.
    hesp_idpiso = models.ForeignKey('Piso', models.DO_NOTHING, db_column='hesp_IdPiso')  # Field name made lowercase.
    hesp_idestanteria = models.ForeignKey(Estanteria, models.DO_NOTHING, db_column='hesp_IdEstanteria')  # Field name made lowercase.
    hesp_idubicacionherr = models.ForeignKey('Ubicacionherramental', models.DO_NOTHING, db_column='hesp_IdUbicacionHerr')  # Field name made lowercase.
    hesp_iddieset = models.ForeignKey(Dieset, models.DO_NOTHING, db_column='hesp_IdDieSet')  # Field name made lowercase.
    hesp_idchatarrizacion = models.ForeignKey(Chatarrizacion, models.DO_NOTHING, db_column='hesp_IdChatarrizacion', blank=True, null=True)  # Field name made lowercase.
    hesp_idordenproduccion = models.ForeignKey('Ordenproduccion', models.DO_NOTHING, db_column='hesp_IdOrdenProduccion', blank=True, null=True)  # Field name made lowercase.
    hesp_idprestamo = models.ForeignKey('Prestamo', models.DO_NOTHING, db_column='hesp_IdPrestamo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HERRAMENTALESPECIFICO'


class Herramentalmaquina(models.Model):
    pk = models.CompositePrimaryKey('mq_IdHerramental', 'mq_IdMaquina')
    mq_idherramental = models.ForeignKey(Herramental, models.DO_NOTHING, db_column='mq_IdHerramental')  # Field name made lowercase.
    mq_idmaquina = models.ForeignKey('Maquina', models.DO_NOTHING, db_column='mq_IdMaquina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HERRAMENTALMAQUINA'


class Imagen(models.Model):
    im_idimagen = models.AutoField(db_column='im_IdImagen', primary_key=True)  # Field name made lowercase.
    im_fechacreacion = models.DateTimeField(db_column='im_FechaCreacion')  # Field name made lowercase.
    im_rutarelativa = models.CharField(db_column='im_RutaRelativa', max_length=255)  # Field name made lowercase.
    im_nombreimagen = models.CharField(db_column='im_NombreImagen', max_length=60)  # Field name made lowercase.
    im_descripcionimagen = models.CharField(db_column='im_DescripcionImagen', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMAGEN'


class Manual(models.Model):
    mn_idmanual = models.AutoField(db_column='mn_IdManual', primary_key=True)  # Field name made lowercase.
    mn_nombremanual = models.CharField(db_column='mn_NombreManual', max_length=100)  # Field name made lowercase.
    mn_fechacreacion = models.DateTimeField(db_column='mn_FechaCreacion')  # Field name made lowercase.
    mn_montaje = models.TextField(db_column='mn_Montaje', blank=True, null=True)  # Field name made lowercase.
    mn_calibracion = models.TextField(db_column='mn_Calibracion', blank=True, null=True)  # Field name made lowercase.
    mn_desmontaje = models.TextField(db_column='mn_Desmontaje', blank=True, null=True)  # Field name made lowercase.
    mn_uso = models.TextField(db_column='mn_Uso', blank=True, null=True)  # Field name made lowercase.
    mn_rutarelativa = models.CharField(db_column='mn_RutaRelativa', max_length=255)  # Field name made lowercase.
    mn_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='mn_IdUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MANUAL'


class Maquina(models.Model):
    ma_idmaquina = models.AutoField(db_column='ma_IdMaquina', primary_key=True)  # Field name made lowercase.
    ma_nummaquina = models.IntegerField(db_column='ma_NumMaquina')  # Field name made lowercase.
    ma_nombremaquina = models.CharField(db_column='ma_NombreMaquina', max_length=30)  # Field name made lowercase.
    ma_anioinstalacion = models.DateField(db_column='ma_AnioInstalacion', blank=True, null=True)  # Field name made lowercase.
    ma_marca = models.CharField(db_column='ma_Marca', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ma_capmaquina = models.FloatField(db_column='ma_CapMaquina', blank=True, null=True)  # Field name made lowercase.
    ma_codigomaquina = models.CharField(db_column='ma_CodigoMaquina', unique=True, max_length=20)  # Field name made lowercase.
    ma_descmaquina = models.CharField(db_column='ma_DescMaquina', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ma_idestadomaquina = models.ForeignKey(Estadomaquina, models.DO_NOTHING, db_column='ma_IdEstadoMaquina')  # Field name made lowercase.
    ma_idtipomaquina = models.ForeignKey('Tipomaquina', models.DO_NOTHING, db_column='ma_IdTipoMaquina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAQUINA'


class Ordenproduccion(models.Model):
    op_idordenproduccion = models.AutoField(db_column='op_IdOrdenProduccion', primary_key=True)  # Field name made lowercase.
    op_consecutivoop = models.CharField(db_column='op_ConsecutivoOp', unique=True, max_length=10)  # Field name made lowercase.
    op_tipodocumentoop = models.CharField(db_column='op_TipoDocumentoOp', max_length=5, blank=True, null=True)  # Field name made lowercase.
    op_numpedido = models.CharField(db_column='op_NumPedido', max_length=10, blank=True, null=True)  # Field name made lowercase.
    op_actividadop = models.CharField(db_column='op_ActividadOp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    op_cantidad = models.DecimalField(db_column='op_Cantidad', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_estadoop = models.CharField(db_column='op_EstadoOp', max_length=30, blank=True, null=True)  # Field name made lowercase.
    op_comentario = models.CharField(db_column='op_Comentario', max_length=500, blank=True, null=True)  # Field name made lowercase.
    op_fechaentregacliente = models.DateTimeField(db_column='op_FechaEntregaCliente', blank=True, null=True)  # Field name made lowercase.
    op_maquinaop = models.CharField(db_column='op_MaquinaOP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    op_idultproducto = models.ForeignKey('Ultimoproducto', models.DO_NOTHING, db_column='op_IdUltProducto', blank=True, null=True)  # Field name made lowercase.
    op_idestproducto = models.ForeignKey('Productoestandar', models.DO_NOTHING, db_column='op_IdEstProducto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDENPRODUCCION'


class Piso(models.Model):
    pi_idpiso = models.AutoField(db_column='pi_IdPiso', primary_key=True)  # Field name made lowercase.
    pi_numeropiso = models.CharField(db_column='pi_NumeroPiso', unique=True, max_length=10)  # Field name made lowercase.
    pi_descripcionpiso = models.CharField(db_column='pi_DescripcionPiso', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PISO'


class Plano(models.Model):
    pl_idplano = models.AutoField(db_column='pl_IdPlano', primary_key=True)  # Field name made lowercase.
    pl_nombreplano = models.CharField(db_column='pl_NombrePlano', max_length=100)  # Field name made lowercase.
    pl_fechacreacion = models.DateTimeField(db_column='pl_FechaCreacion')  # Field name made lowercase.
    pl_rutarelativa = models.CharField(db_column='pl_RutaRelativa', max_length=255)  # Field name made lowercase.
    pl_descripcionplano = models.CharField(db_column='pl_DescripcionPlano', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANO'


class Prestamo(models.Model):
    pr_idprestamo = models.AutoField(db_column='pr_IdPrestamo', primary_key=True)  # Field name made lowercase.
    pr_estadoprestamo = models.CharField(db_column='pr_EstadoPrestamo', max_length=20)  # Field name made lowercase.
    pr_firmarecibe = models.CharField(db_column='pr_FirmaRecibe', max_length=50)  # Field name made lowercase.
    pr_firmaentrega = models.CharField(db_column='pr_FirmaEntrega', max_length=50)  # Field name made lowercase.
    pr_imagenrecibido = models.CharField(db_column='pr_imagenRecibido', max_length=50)  # Field name made lowercase.
    pr_descripcionprestamo = models.CharField(db_column='pr_DescripcionPrestamo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pr_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='pr_IdUsuario')  # Field name made lowercase.
    pr_idordenproduccion = models.ForeignKey(Ordenproduccion, models.DO_NOTHING, db_column='pr_IdOrdenProduccion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTAMO'


class Productoestandar(models.Model):
    pe_idestproducto = models.AutoField(db_column='pe_IdEstProducto', primary_key=True)  # Field name made lowercase.
    pe_nombreestproducto = models.CharField(db_column='pe_NombreEstProducto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pe_a = models.DecimalField(db_column='pe_A', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pe_b = models.DecimalField(db_column='pe_B', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pe_c = models.DecimalField(db_column='pe_C', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pe_d = models.DecimalField(db_column='pe_D', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pe_descripcion = models.CharField(db_column='pe_Descripcion', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTOESTANDAR'


class Propiedadherramental(models.Model):
    ph_idpropiedadherramental = models.AutoField(db_column='ph_IdPropiedadHerramental', primary_key=True)  # Field name made lowercase.
    ph_acero = models.CharField(db_column='ph_Acero', max_length=15)  # Field name made lowercase.
    ph_ttotermico = models.CharField(db_column='ph_TtoTermico', max_length=20)  # Field name made lowercase.
    ph_dureza = models.CharField(db_column='ph_Dureza', max_length=10)  # Field name made lowercase.
    ph_fechacreacion = models.DateTimeField(db_column='ph_FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    ph_proveedor = models.CharField(db_column='ph_Proveedor', max_length=100)  # Field name made lowercase.
    ph_preciototal = models.DecimalField(db_column='ph_PrecioTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ph_descripcion = models.CharField(db_column='ph_Descripcion', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROPIEDADHERRAMENTAL'


class Tipoherramental(models.Model):
    th_idtipoherramental = models.AutoField(db_column='th_IdTipoHerramental', primary_key=True)  # Field name made lowercase.
    th_nombretipoherramental = models.CharField(db_column='th_NombreTipoHerramental', max_length=15)  # Field name made lowercase.
    th_codigotipoherramental = models.CharField(db_column='th_CodigoTipoHerramental', unique=True, max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOHERRAMENTAL'


class Tipomaquina(models.Model):
    tm_idtipomaquina = models.AutoField(db_column='tm_IdTipoMaquina', primary_key=True)  # Field name made lowercase.
    tm_nombretipomaquina = models.CharField(db_column='tm_NombreTipoMaquina', max_length=30)  # Field name made lowercase.
    tm_descripcion = models.CharField(db_column='tm_Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOMAQUINA'


class Tipousuario(models.Model):
    tu_idtipousuario = models.AutoField(db_column='tu_IdTipoUsuario', primary_key=True)  # Field name made lowercase.
    tu_nombretipousuario = models.CharField(db_column='tu_NombreTipoUsuario', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOUSUARIO'


class Ubicacionherramental(models.Model):
    uh_idubicacionherr = models.AutoField(db_column='uh_IdUbicacionHerr', primary_key=True)  # Field name made lowercase.
    uh_numerofila = models.IntegerField(db_column='uh_NumeroFila')  # Field name made lowercase.
    uh_numerocolumna = models.IntegerField(db_column='uh_NumeroColumna')  # Field name made lowercase.
    uh_numeroposicion = models.IntegerField(db_column='uh_NumeroPosicion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UBICACIONHERRAMENTAL'
        unique_together = (('uh_numerofila', 'uh_numerocolumna', 'uh_numeroposicion'),)


class Ultimoproducto(models.Model):
    up_idultproducto = models.AutoField(db_column='up_IdUltProducto', primary_key=True)  # Field name made lowercase.
    up_nombreultproducto = models.CharField(db_column='up_NombreUltProducto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    up_a = models.DecimalField(db_column='up_A', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    up_b = models.DecimalField(db_column='up_B', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    up_c = models.DecimalField(db_column='up_C', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    up_d = models.DecimalField(db_column='up_D', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    up_descripcion = models.CharField(db_column='up_Descripcion', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ULTIMOPRODUCTO'


class Usoherramentaldieset(models.Model):
    pk = models.CompositePrimaryKey('uhd_IdHerramental', 'uhd_IdDieSet', 'uhd_IdMaquina')
    uhd_idherramental = models.ForeignKey(Herramental, models.DO_NOTHING, db_column='uhd_IdHerramental')  # Field name made lowercase.
    uhd_iddieset = models.ForeignKey(Dieset, models.DO_NOTHING, db_column='uhd_IdDieSet')  # Field name made lowercase.
    uhd_idmaquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='uhd_IdMaquina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USOHERRAMENTALDIESET'


class Usoherramentalorden(models.Model):
    pk = models.CompositePrimaryKey('uho_IdHerramental', 'uho_IdOrden')
    uho_idherramental = models.ForeignKey(Herramental, models.DO_NOTHING, db_column='uho_IdHerramental')  # Field name made lowercase.
    uho_idorden = models.ForeignKey(Ordenproduccion, models.DO_NOTHING, db_column='uho_IdOrden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USOHERRAMENTALORDEN'


class Usuario(models.Model):
    us_idusuario = models.AutoField(db_column='us_IdUsuario', primary_key=True)  # Field name made lowercase.
    us_cedula = models.CharField(db_column='us_Cedula', unique=True, max_length=30)  # Field name made lowercase.
    us_nombre = models.CharField(db_column='us_Nombre', max_length=50)  # Field name made lowercase.
    us_apellido = models.CharField(db_column='us_Apellido', max_length=50)  # Field name made lowercase.
    us_celular = models.CharField(db_column='us_Celular', max_length=15, blank=True, null=True)  # Field name made lowercase.
    us_correo = models.CharField(db_column='us_Correo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    us_fechacreacion = models.DateTimeField(db_column='us_FechaCreacion')  # Field name made lowercase.
    us_idtipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='us_IdTipoUsuario')  # Field name made lowercase.
    us_idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='us_IdCargo')  # Field name made lowercase.
    us_user = models.CharField(db_column='us_User', max_length=20, blank=True, null=True)  # Field name made lowercase.
    us_password = models.CharField(db_column='us_Password', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dataqrfile(models.Model):
    prensa = models.IntegerField(db_column='PRENSA', blank=True, null=True)  # Field name made lowercase.
    molde = models.CharField(db_column='MOLDE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alterno = models.CharField(db_column='ALTERNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diametro = models.CharField(db_column='DIAMETRO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    espiga = models.CharField(db_column='ESPIGA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profundidad = models.CharField(db_column='PROFUNDIDAD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maquina_principal = models.CharField(db_column='MAQUINA_PRINCIPAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    opcional = models.CharField(db_column='OPCIONAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porta_pastillas = models.CharField(db_column='PORTA_PASTILLAS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    piso = models.IntegerField(db_column='PISO', blank=True, null=True)  # Field name made lowercase.
    estanteria = models.CharField(db_column='ESTANTERIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fila = models.IntegerField(db_column='FILA', blank=True, null=True)  # Field name made lowercase.
    columna = models.IntegerField(db_column='COLUMNA', blank=True, null=True)  # Field name made lowercase.
    posicion = models.IntegerField(db_column='POSICION', blank=True, null=True)  # Field name made lowercase.
    foto = models.IntegerField(db_column='FOTO', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    existencia_inventario = models.IntegerField(db_column='EXISTENCIA_INVENTARIO', blank=True, null=True)  # Field name made lowercase.
    ruta_imagen = models.CharField(db_column='Ruta_Imagen', max_length=50)  # Field name made lowercase.
    fecha_hora = models.DateTimeField(db_column='Fecha_Hora')  # Field name made lowercase.
    decode_status = models.CharField(db_column='Decode_Status', max_length=50)  # Field name made lowercase.
    error = models.CharField(db_column='Error', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataqrfile'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
