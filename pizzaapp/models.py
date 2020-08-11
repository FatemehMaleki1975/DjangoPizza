from django.db import models

class AdminModel(models.Model):
	username = models.CharField(max_length = 200, null=True)
	password = models.CharField(max_length = 200, null=True)

	def __str__(self) :
		return self.username + " | " + self.password

class PizzaModel(models.Model):
	pizzaName = models.CharField(max_length = 200, null=True)
	pizzaPrice = models.CharField(max_length = 10, null=True)

	def __str__(self):
		return self.pizzaName + " | " + self.pizzaPrice

class  CustomerModel(models.Model):
	userid = models.CharField(max_length =10)
	phoneno = models.CharField(max_length = 10)		

	def __str__(self):
		return self.userid + " | " + self.phoneno

class  OrderModel(models.Model):
	username = models.CharField(max_length =200)
	phoneno = models.CharField(max_length = 10)
	address = models.CharField(max_length = 200)
	ordereditems = models.CharField(max_length =200)		

	def __str__(self):
		return self.username + " | " + self.phoneno + " | " + self.address + " | " + self.ordereditems