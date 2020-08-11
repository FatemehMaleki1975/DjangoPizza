from django.urls import path
from . import views

urlpatterns = [
	path('',views.homepageview, name = 'homepageview'),
	path('homepage/',views.homepageview, name = 'homepageview'),
    path('adminlogin/',views.adminloginview, name = 'adminloginview'),
    path('adminhomepage/',views.adminhomepageview, name = 'adminhomepageview'),
    path('authenticatedadmin/',views.authenticatedadmin, name = 'authenticatedadmin'),
    path('logoutadmin/',views.logoutadmin, name = 'logoutadmin'),
    path('addpizza/',views.addpizza, name = 'addpizza'),
	path('deletepizza/<pizza_id>',views.deletepizza, name = 'deletepizza'),
	path('signupuser/',views.signupuser, name = 'signupuser'),
	path('userlogin/',views.userlogin, name = 'userlogin'),
	path('userauthenticate/',views.userauthenticate, name = 'userauthenticate'),
	path('customerpage/',views.customerpage, name = 'customerpage'),
    path('logoutuser/',views.logoutuser, name = 'logoutuser'),
    path('placeorder/',views.placeorder, name = 'placeorder'),
    path('userorders/',views.userorders, name = 'userorders'),
    path('allorders/',views.allorders, name = 'allorders'),
    path('acceptorder/<orderId>',views.acceptorder, name = 'acceptorder'),
    path('declineorder/<orderId>',views.declineorder, name = 'declineorder'),

]
