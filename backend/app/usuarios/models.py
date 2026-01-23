from django.db import models


class TipoUsuario(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='tu_IdTipoUsuario'
    )
    nombre = models.CharField(
        max_length=20,
        unique=True,
        db_column='tu_NombreTipoUsuario'
    )

    class Meta:
        db_table = 'TIPOUSUARIO'
        managed = False

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='ca_IdCargo'
    )
    nombre = models.CharField(
        max_length=50,
        unique=True,
        db_column='ca_NombreCargo'
    )
    area = models.CharField(
        max_length=30,
        db_column='ca_Area'
    )

    class Meta:
        db_table = 'CARGO'
        managed = False

    def __str__(self):
        return f"{self.nombre} ({self.area})"


class Usuario(models.Model):
    """
    Usuario de negocio (NO auth.User).
    Incluye credenciales propias (temporalmente).
    """

    id = models.AutoField(
        primary_key=True,
        db_column='us_IdUsuario'
    )

    cedula = models.CharField(
        max_length=30,
        unique=True,
        db_column='us_Cedula'
    )

    nombre = models.CharField(
        max_length=50,
        db_column='us_Nombre'
    )

    apellido = models.CharField(
        max_length=50,
        db_column='us_Apellido'
    )

    celular = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        db_column='us_Celular'
    )

    correo = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        db_column='us_Correo'
    )

    fecha_creacion = models.DateTimeField(
        db_column='us_FechaCreacion'
    )

    user = models.CharField(
        max_length=20,
        unique=True,
        db_column='us_User'
    )

    password = models.CharField(
        max_length=20,
        db_column='us_Password'
    )

    tipo_usuario = models.ForeignKey(
        TipoUsuario,
        on_delete=models.PROTECT,
        db_column='us_IdTipoUsuario',
        related_name='usuarios'
    )

    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.PROTECT,
        db_column='us_IdCargo',
        related_name='usuarios'
    )

    class Meta:
        db_table = 'USUARIO'
        managed = False
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.user} - {self.nombre} {self.apellido}"
