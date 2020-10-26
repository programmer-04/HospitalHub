# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amb(models.Model):
    ambid = models.OneToOneField('Hospital', models.DO_NOTHING, db_column='AmbID', primary_key=True)  # Field name made lowercase.
    ambvehicletype = models.CharField(db_column='AmbVehicleType', unique=True, max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Amb'


class Doctor(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctorfirstname = models.CharField(db_column='DoctorFirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doctorlastname = models.CharField(db_column='DoctorLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctor'


class Doctoredu(models.Model):
    doctorid = models.OneToOneField(Doctor, models.DO_NOTHING, db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctordegree = models.CharField(db_column='DoctorDegree', max_length=25)  # Field name made lowercase.
    doctoruni = models.CharField(db_column='DoctorUni', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoctorEdu'
        unique_together = (('doctorid', 'doctordegree'),)


class Doctorspeciality(models.Model):
    doctorid = models.OneToOneField(Doctor, models.DO_NOTHING, db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctorspeciality = models.CharField(db_column='DoctorSpeciality', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoctorSpeciality'
        unique_together = (('doctorid', 'doctorspeciality'),)


class Hosppaymode(models.Model):
    hospid = models.IntegerField(db_column='HospID', blank=True, null=True)  # Field name made lowercase.
    hosppaymode = models.CharField(db_column='HospPayMode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospPayMode'


class Hospphoneno(models.Model):
    hospid = models.IntegerField(db_column='HospID', primary_key=True)  # Field name made lowercase.
    hospphoneno = models.CharField(db_column='HospPhoneNo', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospPhoneNo'
        unique_together = (('hospid', 'hospphoneno'),)


class Hosppincodemodel(models.Model):
    pincode = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='Pincode', blank=True, null=True)  # Field name made lowercase.
    hospcity = models.CharField(db_column='HospCity', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hospcountry = models.CharField(db_column='HospCountry', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospPincode'


class Hospital(models.Model):
    hospid = models.IntegerField(db_column='HospID', primary_key=True)  # Field name made lowercase.
    hospname = models.CharField(db_column='HospName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hospbuilding = models.CharField(db_column='HospBuilding', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hospstreet = models.CharField(db_column='HospStreet', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hosppincode = models.IntegerField(db_column='HospPinCode', unique=True, blank=True, null=True)  # Field name made lowercase.
    hospbeds = models.IntegerField(db_column='HospBeds', blank=True, null=True)  # Field name made lowercase.
    hospavailbed = models.IntegerField(db_column='HospAvailBed', blank=True, null=True)  # Field name made lowercase.
    hospambid = models.IntegerField(db_column='HospAmbID', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hospital'

    def __str__(self):
        return self.hospname

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class User(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    useremailid = models.CharField(db_column='UserEmailID', unique=True, max_length=25)  # Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    userbday = models.DateField(db_column='UserBDay', blank=True, null=True)  # Field name made lowercase.
    usergenderid = models.IntegerField(db_column='UserGenderID', unique=True, blank=True, null=True)  # Field name made lowercase.
    usercity = models.CharField(db_column='UserCity', max_length=25, blank=True, null=True)  # Field name made lowercase.
    userbuilding = models.CharField(db_column='UserBuilding', max_length=25, blank=True, null=True)  # Field name made lowercase.
    userstreet = models.CharField(db_column='UserStreet', max_length=25, blank=True, null=True)  # Field name made lowercase.
    userpincode = models.IntegerField(db_column='UserPinCode', blank=True, null=True)  # Field name made lowercase.
    userprofilepicadd = models.CharField(db_column='UserProfilePicAdd', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Usercomplaint(models.Model):
    userid = models.OneToOneField(User, models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    usercomplaintid = models.IntegerField(db_column='UserComplaintID')  # Field name made lowercase.
    usercomplaintdate = models.DateField(db_column='UserComplaintDate', blank=True, null=True)  # Field name made lowercase.
    usercomplaint = models.CharField(db_column='UserComplaint', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserComplaint'
        unique_together = (('userid', 'usercomplaintid'),)


class Usergender(models.Model):
    genderid = models.OneToOneField(User, models.DO_NOTHING, db_column='GenderID', primary_key=True)  # Field name made lowercase.
    gendername = models.CharField(db_column='GenderName', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserGender'


class Vehicletype(models.Model):
    ambvehicletype = models.OneToOneField(Amb, models.DO_NOTHING, db_column='AmbVehicleType', primary_key=True)  # Field name made lowercase.
    vehiclecap = models.IntegerField(db_column='VehicleCap', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VehicleType'
