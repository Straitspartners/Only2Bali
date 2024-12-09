from django.contrib import admin
from .models import Itinerary

#  the Itinerary will be showed there the user can see all the details they have 
# selected , if they want to change anything they can edit it and in the next page they can confirm the trip. 

class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'confirmed', 'created_at', 'updated_at')
    search_fields = ('user__username', 'status', 'confirmed')
    list_filter = ('status', 'confirmed')
    ordering = ('-created_at',)

admin.site.register(Itinerary, ItineraryAdmin)
