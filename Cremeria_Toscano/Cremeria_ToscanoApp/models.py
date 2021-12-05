from django.db import models

# Create your models here.

class Clientes(models.Model):
    idcliente = models.CharField(db_column='IdCliente', primary_key=True, max_length=4)  # Field name made lowercase.
    idruta = models.ForeignKey('Rutas', models.DO_NOTHING, db_column='IdRuta')  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='NombreCliente', max_length=40)  # Field name made lowercase.
    direccioncliente = models.CharField(db_column='DireccionCliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefonocliente = models.CharField(db_column='TelefonoCliente', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adeudos = models.FloatField(db_column='Adeudos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'

class Compras(models.Model):
    idcompra = models.CharField(db_column='IdCompra', primary_key=True, max_length=4)  # Field name made lowercase.
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='IdProveedor')  # Field name made lowercase.
    fechac = models.DateField(db_column='FechaC')  # Field name made lowercase.
    total = models.FloatField(db_column='Total')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compras'

class Detallescompras(models.Model):
    idcompra = models.OneToOneField(Compras, models.DO_NOTHING, db_column='IdCompra', primary_key=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='IdProducto')  # Field name made lowercase.
    cantidadpc = models.FloatField(db_column='CantidadPC')  # Field name made lowercase.
    costop = models.FloatField(db_column='CostoP')  # Field name made lowercase.
    subtotalc = models.FloatField(db_column='SubTotalC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detallescompras'
        unique_together = (('idcompra', 'idproducto'),)

class Detallesventas(models.Model):
    idventa = models.OneToOneField('Ventas', models.DO_NOTHING, db_column='IdVenta', primary_key=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='IdProducto')  # Field name made lowercase.
    cantidadpv = models.FloatField(db_column='CantidadPV')  # Field name made lowercase.
    costov = models.FloatField(db_column='CostoV')  # Field name made lowercase.
    subtotalv = models.FloatField(db_column='SubTotalV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detallesventas'
        unique_together = (('idventa', 'idproducto'),)

class Productos(models.Model):
    idproducto = models.CharField(db_column='IdProducto', primary_key=True, max_length=4)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='NombreProducto', max_length=40)  # Field name made lowercase.
    cantidadp = models.FloatField(db_column='CantidadP')  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.
    detalles = models.CharField(db_column='Detalles', max_length=60, blank=True, null=True)  # Field name made lowercase.
    stock = models.FloatField(db_column='Stock')  # Field name made lowercase.
    fechacaducidad = models.DateField(db_column='FechaCaducidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'

	#def __str__ (self):
        #return "{}".format(self.nomb)

class Proveedores(models.Model):
    idproveedor = models.CharField(db_column='IdProveedor', primary_key=True, max_length=4)  # Field name made lowercase.
    nomproveedor = models.CharField(db_column='NomProveedor', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedores'

class Rutas(models.Model):
    idruta = models.CharField(db_column='IdRuta', primary_key=True, max_length=4)  # Field name made lowercase.
    idvendedor = models.ForeignKey('Vendedores', models.DO_NOTHING, db_column='IdVendedor')  # Field name made lowercase.
    detalleruta = models.CharField(db_column='DetalleRuta', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rutas'

class Vendedores(models.Model):
    idvendedor = models.CharField(db_column='IdVendedor', primary_key=True, max_length=4)  # Field name made lowercase.
    nombrev = models.CharField(db_column='NombreV', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendedores'

class Ventas(models.Model):
    idventa = models.CharField(db_column='IdVenta', primary_key=True, max_length=4)  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='IdCliente')  # Field name made lowercase.
    fechav = models.DateField(db_column='FechaV')  # Field name made lowercase.
    total = models.FloatField(db_column='Total')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ventas'
