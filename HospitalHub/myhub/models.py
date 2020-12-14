from django.db import models
from django.urls import reverse
import numpy as np


class doctoruni(models.Model):
    name = models.CharField(max_length=200, help_text='Enter your Uni', unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# Create your models here.
class doctoredu(models.Model):
    degree = models.CharField(max_length=200, help_text='Enter degree')
    uni = models.ForeignKey(doctoruni, help_text='Select a uni for this degree', on_delete=models.CASCADE)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.degree + ", " + str(self.uni)

class doctor(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=True)  # Field name made lowercase.
    last_name = models.CharField(max_length=100, blank=False, null=True)  # Field name made lowercase.
    edu = models.ManyToManyField(doctoredu, help_text="Select an education")
    hospital = models.ManyToManyField('hospital', help_text="Select hospital(s):")
    profile= models.ImageField(default ='default.jpg')
    desc = models.CharField(max_length=10000, help_text='Enter Doctor Description', default="No description available for this doctor.")
    speciality = models.CharField(max_length=1000, help_text='Enter Doctor Speciality', default="No speciality available at this moment.") 

    def get_absolute_url(self):
        return reverse('doctors-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.doctor_review_set.all())
        return np.mean(list(all_ratings))
    
    def intaverage_rating(self):
        all_ratings = map(lambda x: x.rating, self.doctor_review_set.all())
        roundedratings = round(np.mean(list(all_ratings)),0).astype(np.int)
        stars = ""
        for i in range(0,roundedratings):
            stars += "*"
        return stars

    class Meta:
        ordering = ['last_name', 'first_name']

class hospital(models.Model):
    name = models.CharField(max_length=100, null=True)  # Field name made lowercase.
    desc = models.CharField(max_length=10000, help_text='Enter Hospital Description')
    building = models.CharField(max_length=25, blank=False, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=25, blank=False, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=25, null=True)  # Field name made lowercase.
    pincode = models.IntegerField(blank=False, null=True)  # Field name made lowercase.
    beds = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    profile= models.ImageField(default ='default.jpg') 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospitals-detail', args=[str(self.id)])

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.hospital_review_set.all())
        return np.mean(list(all_ratings))

    def intaverage_rating(self):
        all_ratings = map(lambda x: x.rating, self.hospital_review_set.all())
        roundedratings = round(np.mean(list(all_ratings)),0).astype(np.int)
        stars = ""
        for i in range(0,roundedratings):
            stars += "*"
        return stars

class ambulance(models.Model):
     class Meta:
      unique_together  = (('key1', 'key2'),)

     key1 = models.ForeignKey(hospital, on_delete=models.CASCADE,)
     key2 = models.IntegerField(primary_key =True)
     ambvehicletype =models.CharField(max_length=25, blank=True, null=True)
     vehiclecapacity =models.IntegerField(blank=True, null=True)
     
class  hospphoneno(models.Model):
      class Meta:
        unique_together  = (('key1', 'phonenumber'),)

      key1 = models.ForeignKey(hospital, on_delete=models.CASCADE,)
      phonenumber= models.CharField(max_length = 10, primary_key =True)
from django.contrib.auth.models import User
    
class doctor_review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('doctors-reviews-detail', args=[str(self.id)])

    def get_rating(self):
        roundedratings = round(self.rating)
        stars = ""
        for i in range(0,roundedratings):
            stars += "*"
        return stars

    def get_date(self):
        return self.pub_date.date()

class hospital_review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('hospitals-reviews-detail', args=[str(self.id)])
        
    def get_rating(self):
        roundedratings = round(self.rating)
        stars = ""
        for i in range(0,roundedratings):
            stars += "*"
        return stars
        

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    profile = models.ImageField(default ='default.jpg')