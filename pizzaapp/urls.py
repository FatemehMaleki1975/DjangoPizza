from django.urls import path
from . import views

urlpatterns = [
    path('adminlogin/',views.adminloginview, name = 'adminloginview'),
    path('adminhomepage/',views.adminhomepageview, name = 'adminhomepageview'),
    path('authenticatedadmin/',views.authenticatedadmin, name = 'authenticatedadmin'),
    path('logoutadmin/',views.logoutadmin, name = 'logoutadmin'),
    path('addpizza/',views.addpizza, name = 'addpizza'),



]
