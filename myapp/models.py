from django.db import models
from django.contrib.auth import get_user_model


class Onibus(models.Model):
	class Meta:
		db_table = "tb_onibus"
	oni_codigo = models.AutoField(auto_created =True, primary_key=True)
	oni_nome = models.CharField(max_length = 50)
	oni_mot_codigo = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
	def __str__(self):
	 	return self.oni_nome
class Coordenadas(models.Model):
    class Meta:
        db_table = 'tb_coordenadas'
    cor_x = models.DecimalField(max_digits=20, decimal_places=17)
    cor_y = models.DecimalField(max_digits=20, decimal_places=17)
    cor_velocidade = models.DecimalField(max_digits=20, decimal_places=17)
    cor_oni_codigo = models.ForeignKey(Onibus, on_delete=models.DO_NOTHING)

class Paradas(models.Model):
	class Meta:
		db_table ="tb_paradas"
	par_codigo = models.AutoField(auto_created=True, primary_key=True)
	par_nome = models.CharField(max_length = 50)
	par_x = models.DecimalField(max_digits = 20, decimal_places=17)
	par_y = models.DecimalField(max_digits = 20, decimal_places=17)
	par_distancia = models.DecimalField(max_digits = 12, decimal_places=2)
	par_oni_codigo = models.ForeignKey(Onibus, on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.par_nome

class Rotas(models.Model):
	class Meta:
		db_table ="tb_rotas"
	rot_codigo = models.AutoField(auto_created=True, primary_key=True)
	rot_x = models.DecimalField(max_digits = 20, decimal_places=17)
	rot_y = models.DecimalField(max_digits = 20, decimal_places=17)
	rot_oni_codigo = models.ForeignKey(Onibus, on_delete=models.DO_NOTHING)
	
class DistanciasR(models.Model):
	class Meta:
		db_table ="tb_distanciasr"
	dis_codigo = models.AutoField(auto_created=True, primary_key=True)
	dis_distancia = models.DecimalField(max_digits = 12, decimal_places=2)
	dis_oni_codigo = models.ForeignKey(Onibus, on_delete=models.DO_NOTHING)

class DistanciaTR(models.Model): #percorrida tempo real
	class Meta:
		db_table ="tb_distanciatr"
	dtr_codigo = models.AutoField(auto_created=True, primary_key=True)
	dtr_distancia = models.DecimalField(max_digits = 12, decimal_places=2)
	dtr_oni_codigo = models.ForeignKey(Onibus, on_delete=models.DO_NOTHING)