create database HospitalHub;
use HospitalHub;
create table Hospital(HospID integer primary key, HospName varchar(100), HospBuilding varchar(25), HospStreet varchar(25), HospPinCode int UNIQUE, HospBeds int, HospAvailBed int, HospAmbID int unique);
create table HospPincode(Pincode integer, foreign key(Pincode) references Hospital(HospPinCode), HospCity varchar(25), HospCountry varchar(25));
create table HospPhoneNo(HospID integer, HospPhoneNo varchar(10), primary key(HospID, HospPhoneNo));
create table HospPayMode(HospID integer, HospPayMode varchar(10));

create table Amb(AmbID int primary key, foreign key(AmbID) references Hospital(HospAmbID), AmbVehicleType varchar(25) unique);
create table VehicleType(AmbVehicleType varchar(25) primary key, foreign key(AmbVehicleType) references Amb(AmbVehicleType), VehicleCap int);

create table User(UserID int primary key, UserEmailID varchar(25) not null unique, UserPhone varchar(10) unique, UserBDay date, UserGenderID int unique, UserCity varchar(25), UserBuilding varchar(25), UserStreet varchar(25), UserPinCode int, UserProfilePicAdd varchar(100));
create table UserGender(GenderID int primary key, foreign key(GenderID) references User(UserGenderID), GenderName varchar(25));
create table UserComplaint(UserID int, UserComplaintID int, foreign key(UserID) references User(UserID), primary key(UserID, UserComplaintID), UserComplaintDate date, UserComplaint varchar(100));

create table Doctor(DoctorID int primary key, DoctorFirstName varchar(100), DoctorLastName varchar(100));
create table DoctorSpeciality(DoctorID int, DoctorSpeciality varchar(100), primary key(DoctorID, DoctorSpeciality), foreign key(DoctorID) references Doctor(DoctorID));
create table DoctorEdu(DoctorID int, DoctorDegree varchar(25), DoctorUni varchar(25), primary key(DoctorID, DoctorDegree), foreign key(DoctorID) references Doctor(DoctorID));

select * from Hospital;
-- Your code here!

