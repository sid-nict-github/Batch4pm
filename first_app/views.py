from django.shortcuts import render
# import HttpResponse
from django.http import HttpResponse
# import the Modelclass from the model
from first_app.models import User
# import the Form
from first_app.forms import CustomerForm, CustomerModelForm

def customer_form_view(request):
    # declare object of the Form
    custform = CustomerModelForm()

    # Step 1: Check if the submit button has been clicked
    # Check if the request method is POST
    if request.method == 'POST':
        # the user has submitted the form
        # Step 2: get the form with data
        # declare a new form object which includes the user input
        custform = CustomerModelForm(request.POST)

        # Step 3: check if the form data is valid
        if custform.is_valid() == True:
            # form is valid / no validation error

            # Step 4: save the form data in the model
            custform.save(commit=True)
            # show confirmation message
            print("Form Submittion successful!")
        else:
            # form is invalid / validation error/s
            # show error message
            print("Error in Form!")

    # dictionary
    d1 = {'custform' : custform}
    # render the template and pass the dictionary with the form object
    return render(request, 'first_app/cform.html', context=d1)

# Create your views here.
# define a function that represents a view
def index(request):
    # create a dictionary
    d1 = {}
    # add key value pairs in it
    d1["keyname"] = "Jaiveer Vardhan Arora"
    d1["keyemail"] = "jaiveer@gmail.com"
    # connect the view and the template
    # open the template file from this view & pass dictionary data
    # return render(request , 'django_app_name/templatename.html' , context=dictionary_name)
    return render(request, 'first_app/tindex.html' , context=d1)


def second(request):
    # create a list of User model records
    # fetch all the records from the model (table) and init. a list
    # listname = ModelClassName.objects.all()
    allusers = User.objects.all()
    # create a dictionary and add the list in it
    d1 = {'allusers' : allusers}
    # render the template and pass the dictionary
    return render(request , 'first_app/tsecond.html' , context=d1)

