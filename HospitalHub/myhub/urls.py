from django.urls import path
from . import views
from django.conf.urls import url, include
urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospitals'),
    path('doctors/<int:doctor_id>', views.DoctorDetailView, name='doctors-detail'),
    path('hospitals/<int:hospital_id>', views.HospitalDetailView, name='hospitals-detail'),
    path('doctors/reviews/<int:pk>', views.DoctorReviewDetailView, name='doctors-reviews-detail'),
    path('hospitals/reviews/<int:pk>', views.HospitalReviewDetailView.as_view(), name='hospitals-reviews-detail'),
   # path('ambulance/', views.ambulanceListView.as_view(), name='doctors'),
    path('doctors/reviews/', views.DoctorReviewListView.as_view()),
    path('hospitals/reviews/', views.HospitalReviewListView.as_view()),
    #path(r'^doctors/(?P<doctor_id>[0-9]+)/add_review/$', views.add_review, name='add_review')
    path('doctors/<int:doctor_id>/add_review', views.doctor_add_review, name='doctor_add_review'),
    path('hospitals/<int:hospital_id>/add_review', views.hospital_add_review, name='hospital_add_review'),

    #url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    url('search', views.search, name="search"),
    path("register/", views.register, name="register"),
    path("enlist/", views.enlist, name = "enlist"),
    path("enlist/doctor", views.enlistdoctor, name="enlistdoctor"),
    path("enlist/hospital", views.enlisthospital, name="enlisthospital"),
    path("enlist/newdegree", views.enlistdegree, name="enlistdegree"),
    path("enlist/newuni", views.enlistuni, name="enlistuni"),

]
'''urlpatterns += [   
    url(r'^doctors/(?P<doctor_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]'''
#urlpatterns +=[url(r'^reviews/', include('review.urls', namespace="reviews")),]
