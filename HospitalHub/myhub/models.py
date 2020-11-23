from django.db import models
from django.urls import reverse
import numpy as np


# Create your models here.
class doctoredu(models.Model):
    degree = models.CharField(max_length=200, help_text='Enter degree')
    uni = models.CharField(max_length=200, help_text='Enter your Uni')
    def __str__(self):
        """String for representing the Model object."""
        return self.degree + "," + self.uni

class doctor(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    edu = models.ManyToManyField(doctoredu, help_text="Select an education")
    hospital = models.ManyToManyField('hospital', help_text="Select hospital(s):")
    profile= models.ImageField(upload_to = 'media',default ='default.jpg') 

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
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, null=True)  # Field name made lowercase.
    desc = models.CharField(max_length=10000, help_text='Enter Hospital Description')
    building = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    pincode = models.IntegerField(unique=True, blank=True, null=True)  # Field name made lowercase.
    beds = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    hospambid = models.IntegerField(unique=True, blank=True, null=True)  # Field name made lowercase.
    profile= models.ImageField(upload_to = 'media',default ='default.jpg') 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospitals-detail', args=[str(self.id)])

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.hospital_review_set.all())
        return np.mean(list(all_ratings))

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
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('doctors-reviews-detail', args=[str(self.id)])

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
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('hospitals-reviews-detail', args=[str(self.id)])
        
 
        

