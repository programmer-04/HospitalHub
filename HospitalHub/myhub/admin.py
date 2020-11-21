from django.contrib import admin

# Register your models here.
from .models import doctor, hospital, doctoredu, review, ambulance, hospphoneno

admin.site.register(doctor)
admin.site.register(hospital)
admin.site.register(doctoredu)
admin.site.register(ambulance)
admin.site.register(hospphoneno)

class ReviewAdmin(admin.ModelAdmin):
    model = review
    list_display = ('doctor', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(review, ReviewAdmin)
