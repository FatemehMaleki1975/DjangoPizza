from django.contrib import admin
from .models import AdminModel,PizzaModel,CustomerModel,OrderModel

admin.site.register(AdminModel)
admin.site.register(PizzaModel)
admin.site.register(CustomerModel)
admin.site.register(OrderModel)

