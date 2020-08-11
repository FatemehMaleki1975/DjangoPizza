from django import forms
from .models import PizzaModel,AdminModel,CustomerModel, OrderModel

class PizzaForm(forms.ModelForm):
	class Meta:
		model = PizzaModel
		fields =["pizzaName","pizzaPrice"]

class AdminForm(forms.ModelForm):
	class Meta:
		model = AdminModel
		fields =["username","password"]

class CustomerForm(forms.ModelForm):
	class Meta:
		model = CustomerModel
		fields =["userid","phoneno"]

class OrderModelForm(forms.ModelForm):
	class Meta:
		model = OrderModel
		fields =["username","phoneno","address","ordereditems"]