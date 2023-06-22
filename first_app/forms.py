# import forms
from django import forms
# import Model
from first_app.models import Customer

# define a class that represents the form
# inherit this class from the built in Form class
class CustomerForm (forms.Form):
    # create the form fields
    # these fields would be the data members of this class
    # form_field_name = forms.CharField()
    # CharField() - is a simple textbox (input type text)
    tname = forms.CharField()
    tphone = forms.CharField()
    temail = forms.EmailField()

# define a class for Model Form
# inherit this class from the built in ModelForm class
class CustomerModelForm(forms.ModelForm):
    # define an inner class - Meta
    class Meta:
        # specify the model to be used
        model = Customer
        # specify the fields to be used in the Model
        fields = ['name' , 'phone' , 'email']
