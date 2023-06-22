from django.contrib import admin
from django.urls import path
# import include
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include the application's urls.py file in here
    # path('AppURLPattern/' , include('appname.urls')),
    path('firstapp/' , include('first_app.urls')),
    path('cbvapp/' , include('cbvapp.urls')),
]
