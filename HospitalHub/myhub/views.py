
from django.shortcuts import render

# Create your views here.
from .models import doctor, doctoredu, hospital, review

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_doctors = doctor.objects.all().count()
    num_hospitals = hospital.objects.all().count()
    
    context = {
        'num_hospitals': num_hospitals,
        'num_doctors': num_doctors,
        }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class DoctorListView(generic.ListView):
    model = doctor

class HospitalListView(generic.ListView):
    model = hospital

class HospitalDetailView(generic.DetailView):
    model = hospital

from .forms import ReviewForm
from django.shortcuts import get_object_or_404

def DoctorDetailView(request, doctor_id):
    Doctor = get_object_or_404(doctor, pk=doctor_id)
    form = ReviewForm()
    return render(request, 'myhub/doctor_detail.html', {'doctor': Doctor, 'form': form})


class ReviewListView(generic.ListView):
    model = review
    #template_name = '/myhub/review_list.html'  # Specify your own template name/location
    queryset = review.objects.order_by('-pub_date')[:9]


class ReviewDetailView(generic.DetailView):
    model=review

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, doctor_id):
    Doctor = get_object_or_404(doctor, pk=doctor_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        #user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        Review = review()
        Review.doctor = Doctor
        Review.user_name = user_name
        Review.rating = rating
        Review.comment = comment
        Review.pub_date = datetime.datetime.now()
        Review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('doctors-detail', args=(Doctor.id,)))

    return render(request, 'myhub/doctor_detail.html', {'doctor': Doctor, 'form': form})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'review_list':latest_review_list, 'username':username}
    return render(request, 'myhub/user_review_list.html', context)

from itertools import chain
from functools import reduce
import operator
from django.db.models import Q
def search(request):        
    if request.method == 'GET': # this will be GET now      
        rawname =  request.GET.get('search') # do some research what it does       
        names = rawname.split()
        print(names)
        '''firstnamematch = doctor.objects.filter(first_name__icontains=name for name in names)
        lastnamematch = doctor.objects.filter(last_name__icontains=name)
        status=list(chain(firstnamematch, lastnamematch))
        '''
        qset1 =  reduce(operator.__or__, [Q(first_name__icontains=name) | Q(last_name__icontains=name) for name in names])
        status = doctor.objects.filter(qset1).distinct()
        # doctor.objects.filter(last_name__icontains=name) # filter returns a list so you might consider skip except part
        return render(request,"myhub/doctor_list.html",{"doctor_list":status})
    return render(request,"myhub/doctor_list.html",{})