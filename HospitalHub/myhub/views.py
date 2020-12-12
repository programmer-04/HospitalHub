
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from .models import doctor, doctoredu, hospital, hospital_review, doctor_review, ambulance, doctoruni

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
from .forms import DoctorReviewForm, HospitalReviewForm
from django.shortcuts import get_object_or_404

class DoctorListView(generic.ListView):
    model = doctor

class HospitalListView(generic.ListView):
    model = hospital

def HospitalDetailView(request, hospital_id):
    Hospital = get_object_or_404(hospital, pk=hospital_id)
    form = DoctorReviewForm()
    return render(request, 'myhub/hospital_detail.html', {'hospital': Hospital, 'form': form})

def DoctorDetailView(request, doctor_id):
    Doctor = get_object_or_404(doctor, pk=doctor_id)
    form = DoctorReviewForm()
    print(Doctor.edu)
    return render(request, 'myhub/doctor_detail.html', {'doctor': Doctor, 'form': form})


class DoctorReviewListView(generic.ListView):
    model = doctor_review
    #template_name = '/myhub/review_list.html'  # Specify your own template name/location
    queryset = doctor_review.objects.order_by('-pub_date')[:9]

class HospitalReviewListView(generic.ListView):
    model = hospital_review
    #template_name = '/myhub/review_list.html'  # Specify your own template name/location
    queryset = hospital_review.objects.order_by('-pub_date')[:9]

'''class DoctorReviewDetailView(generic.DetailView):
    model=doctor_review'''

from django.db import connection
def DoctorReviewDetailView(request, pk):
    'Doctor_review = get_object_or_404(doctor_review, pk=pk)'
    with connection.cursor() as cursor:
            '''cursor.callproc('getdetaildoctor', [1])'''
            cursor.execute("call getdetaildoctor(%s);",[pk])
            Doctor_review = cursor.fetchone()
            username = Doctor_review[2]
            comment = Doctor_review[3]
            starcount = Doctor_review[-2]
            print(Doctor_review)
            stars = ""
            for i in range(0, starcount):
                stars = stars + "*"
            cursor.execute("Select first_name from myhub_doctor where myhub_doctor.id = %s", [Doctor_review[-1]])
            firstname = cursor.fetchone()[0]
            doctorlink = reverse('doctors-detail', args=[Doctor_review[-1]])
            '''return render(request, 'myhub/doctor_review_detail.html', {'doctor_review': Doctor_review})'''
            return render(request, 'myhub/doctor_review_detail.html', {'username': username, 'comment':comment, 'firstname':firstname, 'stars': stars, 'doctorlink':doctorlink})


class HospitalReviewDetailView(generic.DetailView):
    model=hospital_review

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def doctor_add_review(request, doctor_id):
    Doctor = get_object_or_404(doctor, pk=doctor_id)
    form = DoctorReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        #user_name = form.cleaned_data['user_name']
        print(request.user.username)
        user_name = User.objects.get(username=request.user.username)
        Review = doctor_review()
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

@login_required
def hospital_add_review(request, hospital_id):
    Hospital = get_object_or_404(hospital, pk=hospital_id)
    form = HospitalReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        #user_name = form.cleaned_data['user_name']
        user_name = User.objects.get(username=request.user.username)
        Review = hospital_review()
        Review.hospital = Hospital
        Review.user_name = user_name
        Review.rating = rating
        Review.comment = comment
        Review.pub_date = datetime.datetime.now()
        Review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hospitals-detail', args=(Hospital.id,)))

    return render(request, 'myhub/hospital_detail.html', {'hospital': Hospital, 'form': form})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = doctor_review.objects.filter(user_name=username).order_by('-pub_date')
    hospital_review_list = hospital_review.objects.filter(user_name=username).order_by('-pub_date')
    print(username)
    context = {'review_list':latest_review_list, 'username':username, 'hospital_review_list':hospital_review_list}
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
        if names:
            qset1 =  reduce(operator.__or__, [Q(first_name__icontains=name) | Q(last_name__icontains=name) | Q(edu__degree__icontains=name) for name in names])
            doctor_list = doctor.objects.filter(qset1).distinct()
            qset2 = reduce(operator.__or__, [Q(name__icontains=hospname) | Q(city__icontains=hospname) for hospname in names])
            hospital_list = hospital.objects.filter(qset2).distinct()
            # doctor.objects.filter(last_name__icontains=name) # filter returns a list so you might consider skip except part
            return render(request,"myhub/search_list.html",{"doctor_list":doctor_list, "hospital_list":hospital_list})
    return render(request,"myhub/search_list.html",{})
    
#class ambulanceListView(generic.ListView):
     # model = ambulance
from django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return render(request, 'index.html')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                return render(request = request, template_name = "registration.html",context={"form":form})
    form = UserCreationForm
    return render(request = request, template_name = "registration.html",context={"form":form})

from .forms import EnlistDoctorForm, EnlistHospitalForm, AddDegreeForm, AddUniForm
from django.contrib import messages

def enlist(request):
    '''if request.method == "POST":
        if 'doctorform' in request.POST:
            form = EnlistDoctorForm(request.POST, prefix='doctor')
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                hospital = form.cleaned_data['hospital']
                profile = form.cleaned_data['profile']
                edu = form.cleaned_data['edu']
                Doctor = doctor()
                Doctor.first_name = first_name
                Doctor.last_name = last_name
                Doctor.profile = profile
                Doctor.save()
                Doctor.edu.set(edu)
                Doctor.hospital.set(hospital)
                return HttpResponseRedirect(reverse('doctors-detail', args=(Doctor.id,)))
            else:
                for field, items in form.errors.items():
                    for item in items:
                        messages.error(request, '{}: {}'.format(field, item))
                return render(request = request, template_name = "enlist.html",context={"form":form})
        elif 'hospitalform' in request.POST:
            formhospital = EnlistHospitalForm(request.POST, prefix='hospital')   
            if formhospital.is_valid():
                name = formhospital.cleaned_data['name']
                desc = formhospital.cleaned_data['desc']
                building = formhospital.cleaned_data['building']
                street = formhospital.cleaned_data['street']
                pincode = formhospital.cleaned_data['pincode']
                beds = formhospital.cleaned_data['beds']
                profile = formhospital.cleaned_data['profile']
                Hospital = hospital()
                Hospital.name = name
                Hospital.desc = desc
                Hospital.building = building
                Hospital.street = street
                Hospital.pincode = pincode
                Hospital.beds = beds
                Hospital.profile = profile
                Hospital.save()
                return HttpResponseRedirect(reverse('hospitals-detail', args=(Hospital.id,)))
            else:
                for field, items in formhospital.errors.items():
                    for item in items:
                        messages.error(request, '{}: {}'.format(field, item))
                return render(request = request, template_name = "enlist.html",context={"formhospital":formhospital})
    form = EnlistDoctorForm()
    formhospital = EnlistHospitalForm'''
    return render(request = request, template_name = "enlist.html")

def enlistdoctor(request):
    if request.method == "POST":
        form = EnlistDoctorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            hospital = form.cleaned_data['hospital']
            profile = form.cleaned_data['profile']
            edu = form.cleaned_data['edu']
            Doctor = doctor()
            Doctor.first_name = first_name
            Doctor.last_name = last_name
            Doctor.profile = profile
            Doctor.save()
            Doctor.edu.set(edu)
            Doctor.hospital.set(hospital)
            return HttpResponseRedirect(reverse('doctors-detail', args=(Doctor.id,)))
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
                    print('{}: {}'.format(field, item))
            return render(request = request, template_name = "enlistdoctor.html",context={"form":form})
    form = EnlistDoctorForm(request.POST)
    return render(request = request, template_name = "enlistdoctor.html",context={"form":form})

def enlisthospital(request):
    if request.method == "POST":
        formhospital = EnlistHospitalForm(request.POST)   
        if formhospital.is_valid():
            name = formhospital.cleaned_data['name']
            desc = formhospital.cleaned_data['desc']
            building = formhospital.cleaned_data['building']
            street = formhospital.cleaned_data['street']
            pincode = formhospital.cleaned_data['pincode']
            beds = formhospital.cleaned_data['beds']
            profile = formhospital.cleaned_data['profile']
            city = formhospital.cleaned_data['city']
            Hospital = hospital()
            print(name)
            Hospital.name = name
            Hospital.desc = desc
            Hospital.building = building
            Hospital.street = street
            Hospital.pincode = pincode
            Hospital.beds = beds
            Hospital.profile = profile
            Hospital.city=city
            Hospital.save()
            return HttpResponseRedirect(reverse('hospitals-detail', args=(Hospital.id,)))
        else:
            for field, items in formhospital.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
                    print('{}: {}'.format(field, item))
            return render(request = request, template_name = "enlisthospital.html",context={"formhospital":formhospital})
    formhospital = EnlistHospitalForm(request.POST)
    return render(request = request, template_name = "enlisthospital.html",context={"formhospital":formhospital})

def enlistdegree(request):
    if request.method == "POST":
        form = AddDegreeForm(request.POST)
        if form.is_valid():
            degree =form.cleaned_data['degree']
            uni = form.cleaned_data['uni']
            Newdegree = doctoredu()
            Newdegree.degree = degree
            Newdegree.uni = uni
            Newdegree.save()
            return HttpResponseRedirect(reverse('enlist'))
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                return render(request = request, template_name = "enlistdegree.html",context={"form":form})
    form = AddDegreeForm
    return render(request = request, template_name = "enlistdegree.html",context={"form":form})

def enlistuni(request):
    if request.method == "POST":
        form = AddUniForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            NewUni = doctoruni()
            NewUni.name = name  
            NewUni.save()
            return HttpResponseRedirect(reverse('enlist'))
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
                    print('{}: {}'.format(field, item))
            return render(request = request, template_name = "enlistuni.html",context={"form":form})
    form = AddUniForm
    return render(request = request, template_name = "enlistuni.html",context={"form":form})

    