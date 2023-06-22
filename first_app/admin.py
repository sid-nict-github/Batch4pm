from django.contrib import admin
# import User model
from first_app.models import User, Customer, Tag, Product, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)