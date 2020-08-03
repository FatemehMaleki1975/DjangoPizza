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