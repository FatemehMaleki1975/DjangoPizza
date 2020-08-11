from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel, AdminModel, CustomerModel, OrderModel
from django.contrib.auth.models import User
from .forms import PizzaForm, AdminForm, CustomerForm
from django.http import HttpResponseRedirect


def adminloginview(request):
	showLogoutButton = False
	isAdmin = True
	context = {'showLogoutButton': showLogoutButton, 'isAdmin': isAdmin}
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
	isAdmin = True
	# context = {'showLogoutButton':showLogoutButton}
	all_items = PizzaModel.objects.all
	return render(request,'adminhomepage.html',{'showLogoutButton':showLogoutButton, 'pizzas': all_items, 'isAdmin': isAdmin})

def logoutadmin(request):
	logout(request)
	return redirect('adminloginview')

def addpizza(request):
	if not request.user.is_authenticated :
		return redirect('userlogin')
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
	if not request.user.is_authenticated :
		return redirect('userlogin')
	# PizzaModel.objects.filter(id = pizza_id).delete()
	pizza = PizzaModel.objects.get(pk=pizza_id)
	pizza.delete()
	messages.success(request, ('Pizza has been deleted!'))
	return redirect('adminhomepageview')

def homepageview(request):
	return render(request,'homepage.html',{})

def signupuser(request):
	username = request.POST['username']
	password = request.POST['password']
	phoneno = request.POST['phoneno']
	if User.objects.filter(username = username).exists() :
			messages.error(request,('User already exist!'))
			return redirect('homepageview')
	else :
		User.objects.create_user(username = username , password = password).save()
		userId = User.objects.get(username = username).id
		CustomerModel(userid = userId, phoneno = phoneno).save()	
		messages.success(request,('User is successfully created!'))
		return redirect('homepageview')	

	# form = AdminForm(request.POST or None)
	# if form.is_valid():
	# 	if AdminModel.objects.filter(username = request.POST['username']).exists() :
	# 		messages.error(request,('User already exist!'))
	# 		return redirect('homepageview')
	# 	else :	
	# 		form.save()
	# 		userId = AdminModel.objects.get(username = request.POST['username'])
	# 		CustomerModel(userid = userId, phoneno = request.POST['phoneno']).save()	
	# 		messages.success(request,('User is successfully created!'))
	# 		return redirect('homepageview')
	# else:
	# 	messages.success(request,('Information is not valid!!!'))
	# 	return redirect('homepageview')
	

def userlogin(request):
	return render(request,'userlogin.html',{})

def userauthenticate(request):

	username = request.POST['username']
	password = request.POST['password']
	# print(username+'   '+ password)
	user = authenticate(username = username, password = password)

	if user is not None :
		login(request , user)
		return redirect('customerpage')
	if user is None :
		messages.error(request, ('Invalid Credentials!'))
		return redirect('userlogin')

def customerpage(request):
	if not request.user.is_authenticated :
		return redirect('userlogin')
	username = request.user.username
	showLogoutButton = True
	isAdmin = False
	context = {'username': username , 'showLogoutButton':showLogoutButton, 'isAdmin':isAdmin, 'pizzas':PizzaModel.objects.all()}
	return render(request,'customerpage.html',context)

def logoutuser(request):
	logout(request)
	return redirect('userlogin')

def placeorder(request):
	if not request.user.is_authenticated :
		return redirect('userlogin')
	username = request.user.username
	phoneno = CustomerModel.objects.filter(userid = request.user.id )[0].phoneno
	address = request.POST['address']
	print(username + " " + phoneno + " " + address)
	ordereditems = ""
	for pizza in PizzaModel.objects.all():
		pizzaid = pizza.id
		name = pizza.pizzaName
		price = pizza.pizzaPrice
		quantity = request.POST.get(str(pizzaid)," ")
		if str(quantity) != "0" and str(quantity) != " " :
			ordereditems = ordereditems + "Name : "+ name + " " + "Price : "+ str(int(quantity)*int(price)) + " " + "quantity : "+ quantity +"    "
	OrderModel(username = username, phoneno = phoneno, address = address, ordereditems = ordereditems).save()
	messages.success(request,('Order was successfully placed!'))
	return redirect ('customerpage')

def userorders(request):
	if not request.user.is_authenticated or request.user.username == "admin" :
		return redirect ('userlogin')
	showLogoutButton = True
	isAdmin = False
	username = request.user.username	
	orders = OrderModel.objects.filter(username = username)
	context = {'orders' : orders, 'username':username, 'showLogoutButton':showLogoutButton, 'isAdmin':isAdmin}
	return render(request,'userorders.html',context)

def allorders(request):
	if request.user.username == "admin" :
		showLogoutButton = True
		isAdmin = True
		username = request.user.username	
		orders = OrderModel.objects.all()
		context = {'orders' : orders, 'username':username, 'showLogoutButton':showLogoutButton, 'isAdmin':isAdmin}
		return render(request,'allorders.html',context)	
	else:
		return redirect(adminloginview)

def acceptorder(request, orderId):
	order = OrderModel.objects.filter(id = orderId)[0]
	order.status ="accepted"
	order.save()
	# return redirect(allorders)
	return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderId):
	order = OrderModel.objects.filter(id = orderId)[0]
	order.status ="declined"
	order.save()
	# return redirect(allorders)
	return redirect(request.META['HTTP_REFERER'])
