from django.db import models

# Create your models here.
# define a class that represents the data table
# inherit this class from the built in Model class
class User (models.Model):
    # declare the columns of the table as attributes of the class
    # column_name = models.CharField(max_length=n)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # spl. member function __str__() definition
    def __str__(self):
        return self.username + " (" + self.full_name + ")"
    

class Customer (models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Tag (models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Order (models.Model):
    customer = models.ForeignKey(Customer , null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return "Order ID: " + str(self.id) + " ordered on " + str(self.date_ordered)
