from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel
from .forms import PizzaForm
from django.http import HttpResponseRedirect


def adminloginview(request):
	showLogoutButton = False
	context = {'showLogoutButton':showLogoutButton}
	return render(request,'adminlogin.html',context)

def authenticatedadmin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)

	if user is not None and user.username == "admin" :
		# user exist
		login(request , user)
		return redirect('adminhomepageview')
	if user is None :
		# user does not exist
		# messages.add_message(request, messages.ERROR,"Invalid Credentials")
		messages.error(request, ('Invalid Credentials!'))
		return redirect('adminloginview')

def adminhomepageview(request):
	showLogoutButton = True
	context = {'showLogoutButton':showLogoutButton}
	all_items = PizzaModel.objects.all
	return render(request,'adminhomepage.html',{'showLogoutButton':showLogoutButton, 'pizzas': all_items})

def logoutadmin(request):
	logout(request)
	return redirect('adminloginview')

def addpizza(request):
	# name = request.POST['pizzaName']
	# price = request.POST['pizzaPrice']
	# PizzaModel(pizzaName = name , pizzaPrice = price).save

	if request.method == 'POST':
		form = PizzaForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ('Pizza has been Added To list!'))
	return redirect ('adminhomepageview')

def deletepizza(request,pizza_id):
	pizza = PizzaModel.objects.get(pk=pizza_id)
	pizza.delete()
	messages.success(request, ('Pizza has been deleted!'))
	return redirect('adminhomepageview')


	