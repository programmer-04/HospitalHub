from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hospital/', views.hospitalListView.as_view(), name='hospital'),
    path('hospital/<int:pk>', views.hospitalDetailView.as_view(), name='hospital-detail'),
    path('doctor/', views.doctorListView.as_view(), name='doctor'),
    path('doctor/<int:pk>', views.doctorDetailView.as_view(), name='doctor-detail'),
]