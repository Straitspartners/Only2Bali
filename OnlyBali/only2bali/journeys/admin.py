from django.contrib import admin
from .models import (
    JourneyPreferences, 
    PlacesToVisit, 
    TravelDetails, 
    StayPreferences, 
    FoodPreferences, 
    VehiclePreferences, 
    TourGuidePreferences, 
    CateringOrChef, 
    PaperworkAssistance, 
    Vendor, 
    ExtraRequests
)

# Registering all models
admin.site.register(JourneyPreferences)
admin.site.register(PlacesToVisit)
admin.site.register(TravelDetails)
admin.site.register(StayPreferences)
admin.site.register(FoodPreferences)
admin.site.register(VehiclePreferences)
admin.site.register(TourGuidePreferences)
admin.site.register(CateringOrChef)
admin.site.register(PaperworkAssistance)
admin.site.register(Vendor)
admin.site.register(ExtraRequests)
