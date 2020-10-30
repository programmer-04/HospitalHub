from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse

# Create your views here.

from MyHub.models import Amb, Doctor, Doctoredu, Doctorspeciality, Hosppaymode, Hospphoneno, Hosppincodemodel, hospital, User, Usercomplaint, Usergender, Vehicletype

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_hosps = hospital.objects.all().count()
    num_doctors = Doctor.objects.all().count()
    
    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_users = User.objects.count()
    
    context = {
        'num_hosps': num_hosps,
        'num_doctors': num_doctors,
        #'num_instances_available': num_instances_available,
        'num_users': num_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class hospitalListView(generic.ListView):
    model = hospital

class hospitalDetailView(generic.DetailView):
    model = hospital    
<<<<<<< HEAD
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
=======

class doctorListView(generic.ListView):
    model = Doctor    

class doctorDetailView(generic.DetailView):
    model = Doctor 
>>>>>>> 3a6dc714066642d44e9ecf7fa1f23b462ed79b70
