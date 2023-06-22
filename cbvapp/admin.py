from django.contrib import admin
from cbvapp.models import School

# define a class with the name ModelnameAdmin
# and inherit this class from the ModelAdmin class
class SchoolAdmin(admin.ModelAdmin):
    # for re-ordering fields, add the following
    # fields = ['model_field_name', 'model_field_name']
    fields = ['name','location','principal']
    # for implementing search, add the following
    # search_fields = ['model_field_name']
    search_fields = ['name', 'location']
    # for adding filters, add the following code
    # list_filter = ['model_field_name']
    list_filter = ['location']
    # for adding fields, add the following code
    # list_display = ['model_field_name','model_field_name']
    list_display = ['name','principal','location']
    # for editable list views, add the following code
    # list_editable = ['model_field_name']
    list_editable = ['principal']



# Register your models here.
admin.site.register(School, SchoolAdmin)