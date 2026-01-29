from django.db import models

class DataQRFile(models.Model):
    # Django agregará automáticamente un campo 'id' como clave primaria.
    # Si la tabla ya tiene una PK, deberás especificarla aquí.

    prensa = models.IntegerField(db_column='PRENSA', null=True, blank=True)
    molde = models.CharField(primary_key=True, max_length=50, db_column='MOLDE') # Asumo que este es obligatorio
    alterno = models.CharField(max_length=50, db_column='ALTERNO', null=True, blank=True)
    diametro = models.CharField(max_length=50, db_column='DIAMETRO', null=True, blank=True)
    espiga = models.CharField(max_length=50, db_column='ESPIGA', null=True, blank=True)
    profundidad = models.CharField(max_length=100, db_column='PROFUNDIDAD', null=True, blank=True)
    maquina_principal = models.CharField(max_length=50, db_column='MAQUINA_PRINCIPAL', null=True, blank=True)
    opcional = models.CharField(max_length=50, db_column='OPCIONAL', null=True, blank=True)
    porta_pastillas = models.CharField(max_length=50, db_column='PORTA_PASTILLAS', null=True, blank=True)
    piso = models.IntegerField(db_column='PISO', null=True, blank=True)
    estanteria = models.CharField(max_length=50, db_column='ESTANTERIA', null=True, blank=True)
    fila = models.IntegerField(db_column='FILA', null=True, blank=True)
    columna = models.IntegerField(db_column='COLUMNA', null=True, blank=True)
    posicion = models.IntegerField(db_column='POSICION', null=True, blank=True)
    foto = models.IntegerField(db_column='FOTO', null=True, blank=True)
    descripcion = models.CharField(max_length=100, db_column='DESCRIPCION', null=True, blank=True)
    observaciones = models.CharField(max_length=50, db_column='OBSERVACIONES', null=True, blank=True)
    estado = models.CharField(max_length=50, db_column='ESTADO', null=True, blank=True)
    existencia_inventario = models.IntegerField(db_column='EXISTENCIA_INVENTARIO', null=True, blank=True)
    ruta_imagen = models.CharField(max_length=50, db_column='Ruta_Imagen', null=True, blank=True)
    # 'auto_now_add=True' guardará la fecha y hora actual automáticamente al crear el registro
    fecha_hora = models.DateTimeField(db_column='Fecha_Hora', auto_now_add=True)
    decode_status = models.CharField(max_length=50, db_column='Decode_Status', null=True, blank=True)
    error = models.CharField(max_length=50, db_column='Error', null=True, blank=True)

    class Meta:
        db_table = 'dataqrfile' # Nombre exacto de la tabla en SQL Server
        verbose_name = 'Archivo de Datos QR'
        verbose_name_plural = 'Archivos de Datos QR'
        managed = False  # Indica que Django no debe gestionar la creación de esta tabla

    def __str__(self):
        # Devuelve una representación legible del objeto, por ejemplo, el nombre del molde
        return self.molde