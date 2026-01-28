from django.db import models

class Piso(models.Model):
    pi_IdPiso = models.AutoField(primary_key=True, db_column='pi_IdPiso')
    pi_NumeroPiso = models.CharField(max_length=10, unique=True, db_column='pi_NumeroPiso')
    pi_DescripcionPiso = models.CharField(max_length=255, null=True, blank=True, db_column='pi_DescripcionPiso')

    class Meta:
        db_table = 'PISO'
        managed = False


    def __str__(self):
        return self.pi_NumeroPiso



class Estanteria(models.Model):
    es_IdEstanteria = models.AutoField(primary_key=True, db_column='es_IdEstanteria')
    es_NombreEstanteria = models.CharField(max_length=50, unique=True, db_column='es_NombreEstanteria')
    # Relación con Piso

    #piso = models.ForeignKey(Piso, models.DO_NOTHING)

    piso = models.ForeignKey(
        Piso, 
        on_delete=models.PROTECT, 
        db_column='es_IdPiso', 
        related_name='estanterias'
    )

    class Meta:
        db_table = 'ESTANTERIA'
        managed = False


    def __str__(self):
        return self.es_NombreEstanteria