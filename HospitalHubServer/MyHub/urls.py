<<<<<<< HEAD
from django .urls import path
from  .import views

urlspatterns =[

]
=======
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hospital/', views.hospitalListView.as_view(), name='hospital'),
    path('hospital/<int:pk>', views.hospitalDetailView.as_view(), name='hospital-detail'),
<<<<<<< HEAD
]
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
=======
    path('doctor/', views.doctorListView.as_view(), name='doctor'),
    path('doctor/<int:pk>', views.doctorDetailView.as_view(), name='doctor-detail'),
]
>>>>>>> 3a6dc714066642d44e9ecf7fa1f23b462ed79b70
