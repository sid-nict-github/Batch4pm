from django.shortcuts import render
# import View class
from django.views.generic import View
# import TemplateView class
from django.views.generic import TemplateView
# import HttpResponse
from django.http import HttpResponse
# ListView Step 0: import the Model class
from cbvapp.models import School
# ListView Step 1: import the ListView class
from django.views.generic import ListView
# DetailView Step 1: import the DetailView class
from django.views.generic import DetailView
# CreateView Step 1: import CreateView
from django.views.generic.edit import CreateView
# DeleteView Step 1: import DeleteView & reverse_lazy
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# UpdateView Step 1: import UpdateView
from django.views.generic.edit import UpdateView

# import requests
import requests

def view_comments(request):
    # fetch the data from the API and decode the data in JSON form
    # response_object = requests.get('url').json()
    response = requests.get('https://jsonplaceholder.typicode.com/comments').json()
    # render the template and send the response as context
    return render(request, 'cbvapp/view_comments.html',{'response': response})


# UpdateView Part 2: Create a View for the success_url template page:
class SchoolUpdationSuccess (TemplateView):
    template_name = 'cbvapp/school_updation_success.html'

# UpdateView Part 4: Create a view for Updation:
# Step 2: define a class based view for updation and inherit it from the UpdateView:
class SchoolUpdateView(UpdateView):
    # Step 3: set the model
    model = School
    # Step 4: choose which model fields to display in the updation form
    fields = ('name','principal','location')
    # Step 5: Specify the success_url (the url to redirect to after successful updation)
    success_url = reverse_lazy('school_updation_success')


# DeleteView Step 2: define a class based view to perform deletion 
# & inherit this class from the DeleteView class:
class SchoolDeleteView (DeleteView):
    # DeleteView Step 3: associate the ViewClass with the model
    model = School
    # DeleteView Step 4: setup the success URL
    success_url = reverse_lazy('school-list')
    


# CreateView Step 2: define a Class Based View for insertion and 
# extend / inherit it from the CreateView:
class SchoolCreateView (CreateView):
    # CreateView Step 3: associate the ViewClass with the Template file:
    template_name = 'cbvapp/create_school.html'
    # CreateView Step 4: associate the ViewClass with the model
    model = School
    # CreateView Step 5: choose the fields from the model to be present in the model
    fields = ('name','principal','location')


# DetailView Step 2: create a View class and extend / 
# inherit it from the DetailView class
class SchoolDetailView (DetailView):
    # DetailView Step 3: associate the ViewClass with the Template file:
    template_name = 'cbvapp/school_detail.html'
    # DetailView Step 4: associate the ViewClass with the model
    model = School
    # DetailView Step 5: set the name of the list that would be accessed in the HTML file.
    context_object_name = 'school_detail'

# ListView Step 2: define a View Class and inherit it from the ListView class:
class SchoolListView (ListView):
    # ListView Step 3: associate the ViewClass with the Template file:
    template_name = 'cbvapp/school_list.html'
    # ListView Step 4: associate the ViewClass with the model
    model = School
    # ListView Step 5: set the name of the list that would be accessed in the HTML file
    context_object_name = 'schools'


# Create your views here.
# define a class base view
# inherit this class from the built in View class
class FirstView (View):
    # to display some message via response, define member function - get()
    # get() takes the request as argument
    def get(self, request):
        # display some message as response
        return HttpResponse("Welcome to Class based Views.")

# define a class based view having template
# inherit from TemplateView
class SecondView (TemplateView):
    # define the template_name
    template_name = 'cbvapp/second.html'
    # define a member function of the TemplateView class – get_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # populate the context dictionary with data
        context["name"] = "Jaiveer Vardhan Arora"
        context["phone"] = "+919898989898"
        context["email"] = "jaiveervardhanarora@gmail.com"
        # return the dictionary context
        return context