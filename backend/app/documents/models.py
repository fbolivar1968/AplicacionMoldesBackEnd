import os
from datetime import datetime
from django.db import models

def upload_to_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Usamos el nombre que viene del modelo para el archivo físico
    nombre = getattr(instance, 'nombre_imagen', None) or getattr(instance, 'NombrePlano', None) or getattr(instance, 'NombreManual', None) or "archivo"
    nombre_limpio = str(nombre).replace(" ", "_")
    nuevo_nombre = f"{timestamp}_{nombre_limpio}.{ext}"

    folders = {'pdf': 'pdf', 'jpg': 'imagenes', 'jpeg': 'imagenes', 'png': 'imagenes', 'docx': 'docs', 'doc': 'docs'}
    folder = folders.get(ext, 'others')
    return os.path.join(folder, nuevo_nombre)

class Imagen(models.Model):
    # En el modelo se llama 'id_imagen', pero en SQL Server es 'im_IdImagen'
    id_imagen = models.AutoField(primary_key=True, db_column='im_IdImagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='im_FechaCreacion')
    ruta_relativa = models.FileField(upload_to=upload_to_path, max_length=255, db_column='im_RutaRelativa')
    nombre_imagen = models.CharField(max_length=60, db_column='im_NombreImagen')
    descripcion_imagen = models.CharField(max_length=500, blank=True, null=True, db_column='im_DescripcionImagen')

    class Meta:
        db_table = 'IMAGEN'
        managed = False  # Como la tabla ya existe en SQL Server


class Plano(models.Model):
    IdPlano = models.AutoField(primary_key=True, db_column='pl_IdPlano')
    NombrePlano = models.CharField(max_length=60, db_column='pl_NombrePlano')
    FechaCreacion = models.DateTimeField(auto_now_add=True, db_column='pl_FechaCreacion')
    DescripcionPlano = models.CharField(max_length=500, blank=True, null=True, db_column='pl_DescripcionPlano')
    RutaRelativaPlano = models.FileField(upload_to=upload_to_path, max_length=255, db_column='pl_RutaRelativa')

    class Meta:
        db_table = 'PLANO'
        managed = False


class Manual(models.Model):
    IdManual = models.AutoField(primary_key=True, db_column='ma_IdManual')
    NombreManual = models.CharField(max_length=60, db_column='ma_NombreManual')
    FechaCreacion = models.DateTimeField(auto_now_add=True, db_column='ma_FechaCreacion')
    DescripcionManual = models.CharField(max_length=500, blank=True, null=True, db_column='ma_DescripcionManual')
    RutaRelativaManual = models.FileField(upload_to=upload_to_path, max_length=255, db_column='ma_RutaRelativa')

    class Meta:
        db_table = 'MANUAL'
        managed = False