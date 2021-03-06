from django.db import models

# Create your models here.

class Prototype(models.Model):
	nama_ketua			= models.CharField(max_length=100)
	email	  			= models.EmailField(max_length=100)
	no_telepon 			= models.CharField(max_length=100)
	instansi			= models.CharField(max_length=100)
	prodi_ketua			= models.CharField(max_length=100)
	nama_anggota		= models.CharField(max_length=100)
	prodi_anggota		= models.CharField(max_length=100)
	subtema				= models.CharField(max_length=100)

	def __str__(self):
		return "{}".format(self.subtema)

	class Meta:
		db_table = "Prototype"