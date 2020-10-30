"""HospitalHubServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
  
]
# Use include() to add paths from the catalog application



=======
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# Use include() to add paths from the catalog application 
from django.urls import include

urlpatterns += [
    path('MyHub/', include('MyHub.urls')),
]
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='MyHub/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
<<<<<<< HEAD
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
=======

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
>>>>>>> 3a6dc714066642d44e9ecf7fa1f23b462ed79b70
