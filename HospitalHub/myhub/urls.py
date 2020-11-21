from django.urls import path
from . import views
from django.conf.urls import url, include
urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospitals'),
    path('doctors/<int:doctor_id>', views.DoctorDetailView, name='doctors-detail'),
    path('hospitals/<int:pk>', views.HospitalDetailView.as_view(), name='hospitals-detail'),
    path('reviews/<int:pk>', views.ReviewDetailView.as_view(), name='reviews-detail'),
   # path('ambulance/', views.ambulanceListView.as_view(), name='doctors'),
    path('reviews/', views.ReviewListView.as_view(), name='ambulance',),
    #path(r'^doctors/(?P<doctor_id>[0-9]+)/add_review/$', views.add_review, name='add_review')
    path('doctors/<int:doctor_id>/add_review', views.add_review, name='add_review'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    url('search', views.search, name="search")
]
'''urlpatterns += [   
    url(r'^doctors/(?P<doctor_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]'''
#urlpatterns +=[url(r'^reviews/', include('review.urls', namespace="reviews")),]
