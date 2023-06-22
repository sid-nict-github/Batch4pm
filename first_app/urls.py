# import path
from django.urls import path
# import views module from first_app's views
from first_app import views

# define the urlpatterns
urlpatterns = [
    path('home' , views.index),
    path('2nd' , views.second),
    path('cform', views.customer_form_view),
]