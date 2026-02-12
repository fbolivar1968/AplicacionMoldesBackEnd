from django.db import models

# Create your models here.
# Modelo para la vista VW_OrdenesPro
class OrdenProduccionForja(models.Model):
    codigo_herramental = models.CharField(null=True, blank=True,max_length=1024, db_column='Codigo Herramental')
    numero_pedido = models.CharField(max_length=20, db_column='Numero de Pedido')
    consecutivo_op = models.CharField(max_length=20, primary_key=True, db_column='Orden de Produccion')
    estado_op = models.CharField(max_length=20, db_column='Estado OP')
    fecha_inicio = models.DateTimeField(db_column='Fecha de Inicio')
    comentario = models.TextField(null=True, blank=True, db_column='Comentario')
    producto = models.TextField(null = True, max_length=50, db_column='Producto')


    class Meta:
        db_table = 'v_plantaVirtual'
        managed = False
        ordering = ['-fecha_inicio']