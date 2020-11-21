from django.contrib import admin

# Register your models here.
from .models import doctor, hospital, doctoredu, review

admin.site.register(doctor)
admin.site.register(hospital)
admin.site.register(doctoredu)

class ReviewAdmin(admin.ModelAdmin):
    model = review
    list_display = ('doctor', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(review, ReviewAdmin)