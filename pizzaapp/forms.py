from django import forms
from .models import PizzaModel

class PizzaForm(forms.ModelForm):
	class Meta:
		model = PizzaModel
		fields =["pizzaName","pizzaPrice"]