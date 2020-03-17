from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Localidad(models.Model):
	id_localidad = models.AutoField(db_column='id_localidad', primary_key=True)
	nombre_localidad = models.CharField(max_length=15,db_column='nombre_localidad')

	def __str__(self):
		return '{}'.format(self.nombre_localidad)

	class Meta:
		managed = True
		db_table = 'localidad'
		


class PuntoVenta(models.Model):
	status = [
	("ACTIVO", 'Activo'),
	("INACTIVO", 'Inactivo')

]

	id_pv = models.AutoField(db_column='id_pv', primary_key=True)  # Field name made lowercase.
	nombre_pv = models.CharField(max_length=50,blank=True,null=True)  # Field name made lowercase.
	estado_pv = models.CharField(max_length=10,choices=status,default="activo",db_column='estado_pv')  # Field name made lowercase.
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	id_localidad = models.ForeignKey('localidad',on_delete=models.CASCADE,db_column='id_localidad') # Field name made lowercase

	def __str__(self):
		return '{}'.format(self.nombre_pv)

	def save(self):
		self.nombre_pv = self.nombre_pv.upper()
		self.estado_pv = self.estado_pv.upper()
		#self.localidad = self.localidad.upper()
		super(PuntoVenta, self).save()

	class Meta:
		managed = True
		db_table = 'punto_venta'

class PosPc(models.Model):
	status = [
	("ACTIVO", 'Activo'),
	("INACTIVO", 'Inactivo')
	]

	id_pos_pc = models.AutoField(db_column='id_pos_pc', primary_key=True)  # Field name made lowercase.
	codigo_pos_pc = models.IntegerField(db_column='codigo_pos_pc')  # Field name made lowercase.
	estado_pos_pc = models.CharField(max_length=10,choices=status,default="activo",db_column='estado_pos_pc')  # Field name made lowercase.
	id_pv = models.ForeignKey('PuntoVenta', models.DO_NOTHING, db_column='id_pv')  # Field name made lowercase.
	
	def __str__(self):
		return '{}'.format(self.codigo_pos_pc)

	def save(self):
		self.estado_pos_pc = self.estado_pos_pc.upper()
		super(PosPc, self).save()

	class Meta:
		managed = True
		db_table = 'pos_pc'



class Cajero(models.Model):
	status = [
	("ACTIVO", 'Activo'),
	("INACTIVO", 'Inactivo')
	]
	id_cajero = models.AutoField(db_column='id_cajero', primary_key=True)  # Field name made lowercase.
	nombre_cajero = models.CharField(max_length=15,db_column='nombre_cajero')  # Field name made lowercase.
	clave_cajero = models.CharField(max_length=15,db_column='clave_cajero')  # Field name made lowercase.
	estado_cajero = models.CharField(max_length=10,choices=status,default="activo",db_column='estado_cajero')  # Field name made lowercase.
	id_pos_pc = models.ForeignKey('PosPc', models.DO_NOTHING, db_column='id_pos_pc')  # Field name made lowercase.

	def save(self):
		self.nombre_cajero = self.nombre_cajero.upper()
		self.estado_cajero = self.estado_cajero.upper()
		super(Cajero, self).save()
	
	class Meta:
		managed = True
		db_table = 'cajero'

class Sorteos(models.Model):
	id_sorteos = models.AutoField(db_column='id_sorteos', primary_key=True)  # Field name made lowercase.
	numeros_sorteos = models.IntegerField(db_column='numeros_sorteos')  # Field name made lowercase.
	bonos = models.TextField(db_column='BONOS')  # Field name made lowercase.
	carta_ganadora = models.IntegerField(db_column='carta_ganadora')  # Field name made lowercase.
	fecha_sorteos = models.TextField(db_column='fecha_sorteos')  # Field name made lowercase.
	hora_sorteos = models.TextField(db_column='hora_sorteos')  # Field name made lowercase.
	estado_sorteos = models.TextField(db_column='estado_sorteos')  # Field name made lowercase.
	numero_carta = models.IntegerField(db_column='numero_carta')  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'SORTEOS'

class CartonCartas(models.Model):
	id_c_c = models.AutoField(db_column='id_c_c', primary_key=True)  # Field name made lowercase.
	alta_baja = models.TextField(db_column='alta_baja')  # Field name made lowercase.
	color = models.TextField(db_column='COLOR')  # Field name made lowercase.
	valor_apuesta_c = models.IntegerField(db_column='valor_apuesta_c')  # Field name made lowercase.
	fecha_cartas = models.TextField(db_column='fecha_cartas')  # Field name made lowercase.
	hora_cartas = models.TextField(db_column='hora_cartas')  # Field name made lowercase.
	id_sorteos = models.ForeignKey('Sorteos', models.DO_NOTHING, db_column='id_sorteos', null=True)  # Field name made lowercase.
	id_cajero = models.ForeignKey('Cajero', models.DO_NOTHING, db_column='id_cajero', null=True)  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'carton_cartas'


class CartonKeno(models.Model):
	id_c_k = models.AutoField(db_column='id_c_k', primary_key=True)  # Field name made lowercase.
	apuesta_keno = models.TextField(db_column='apuesta_keno')  # Field name made lowercase.
	valor_apuesta_k = models.IntegerField(db_column='valor_apuesta_k')  # Field name made lowercase.
	fecha_keno = models.TextField(db_column='fecha_keno')  # Field name made lowercase.
	hora_keno = models.TextField(db_column='hora_keno')  # Field name made lowercase.
	id_sorteos = models.ForeignKey('Sorteos', models.DO_NOTHING, db_column='id_sorteos', null=True)  # Field name made lowercase.
	id_cajero = models.ForeignKey('Cajero', models.DO_NOTHING, db_column='id_cajero', null=True)  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'carton_keno'


class GanadoresCartas(models.Model):
	id_ganadores_c = models.AutoField(db_column='id_ganadores_c', primary_key=True)  # Field name made lowercase.
	valor_ganado_c = models.IntegerField(db_column='valor_ganado_c')  # Field name made lowercase.
	fecha_ganadores_c = models.TextField(db_column='fecha_ganadores_c')  # Field name made lowercase.
	hora_ganadores_c = models.TextField(db_column='hora_ganadores_c')  # Field name made lowercase.

   # id_c_c = models.ForeignKey(CartonCartas, models.DO_NOTHING, db_column='id_c_c')  # Field name made lowercase.

	id_c_c = models.ForeignKey('CartonCartas', models.DO_NOTHING, db_column='id_c_c')  # Field name made lowercase.


	class Meta:
		managed = True
		db_table = 'ganadores_cartas'


class GanadoresJackpot(models.Model):
	id_ganadores_j = models.AutoField(db_column='id_ganadores_j', primary_key=True)  # Field name made lowercase.
	valor_ganado_j = models.IntegerField(db_column='valor_ganado_j')  # Field name made lowercase.
	fecha_ganadores_j = models.TextField(db_column='fecha_ganadores_j')  # Field name made lowercase.
	hora_ganadores_j = models.TextField(db_column='hora_ganadores_j')  # Field name made lowercase.
	id_c_k = models.IntegerField(db_column='ID_C_K')  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'ganadores_jackpot'


class GanadoresKeno(models.Model):
	id_ganadores_k = models.AutoField(db_column='id_ganadores_k', primary_key=True)  # Field name made lowercase.
	valor_ganado_k = models.IntegerField(db_column='valor_ganado_k')  # Field name made lowercase.
	fecha_ganadores_k = models.TextField(db_column='fecha_ganadores_k')  # Field name made lowercase.
	hora_ganadores_k = models.TextField(db_column='hora_ganadores_k')  # Field name made lowercase.
	# id_c_k = models.IntegerField(db_column='ID_C_K')  # Field name made lowercase.
	id_c_k = models.ForeignKey('CartonKeno', models.DO_NOTHING, db_column='id_c_k')  # Field name made lowercase.

	class Meta:
		managed = True
		db_table = 'ganadores_keno'


class Jackpot(models.Model):
	id_jackpot = models.AutoField(db_column='id_jackpot', primary_key=True)  # Field name made lowercase.
	monto_actual = models.IntegerField(db_column='monto_actual')  # Field name made lowercase.
	monto_activacion_j = models.IntegerField(db_column='monto_activacion_j')  # Field name made lowercase.
	activacion_bono = models.IntegerField(db_column='activacion_bono')  # Field name made lowercase.
	aumento_jackpot = models.FloatField(db_column='aumento_jackpot')  # Field name made lowercase.
	
	class Meta:
		managed = True
		db_table = 'jackpot'




