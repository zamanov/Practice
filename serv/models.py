from django.db import models

# Create your models here.
class Cell(models.Model):
	cell_name = models.CharField(max_length = 30)
	is_blocked = models.BooleanField(default = False)
	sector = models.IntegerField(default = 0)
	row = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.cell_name
		
class Object(models.Model):
	object_name = models.CharField(max_length = 30)
	cell = models.ForeignKey(Cell)
	owner = models.CharField(max_length = 30, default = "admin")
	def __unicode__(self):
		return self.object_name
