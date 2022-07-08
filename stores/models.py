from django.db import models
from django.contrib.auth.models import User


class store(models.Model):
	name = models.ForeignKey(User,on_delete=models.PROTECT)
	store_name = models.CharField(max_length=30,unique=True)


	def __str__(self):
		return self.store_name

class books(models.Model):
	choices = {
	'Horror', 'Horror',
	'Love' , 'Love',
	'Regional' , 'Regional',
	'Pedatric' , 'Pedatric'
	}
	store_id = models.ForeignKey(store,on_delete=models.CASCADE)
	auther = models.CharField(max_length=20)
	book_name = models.CharField(max_length=20,unique=True)
	book_type = models.CharField(max_length=20)
	stock = models.IntegerField(null=False,default=1)



	def __str__(self):
		return self.book_name + " store name  " +str(self.store_id)