from django.db import models
from users.models import CustomUser
from journeys.models import JourneyPreferences, TravelDetails, StayPreferences, FoodPreferences, VehiclePreferences, TourGuidePreferences, PaperworkAssistance, ExtraRequests , Vendor , CateringOrChef

class Itinerary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    travel_details = models.OneToOneField(TravelDetails, on_delete=models.CASCADE)
    stay_preferences = models.OneToOneField(StayPreferences, on_delete=models.CASCADE)
    food_preferences = models.ManyToManyField(FoodPreferences)
    vehicle_preferences = models.OneToOneField(VehiclePreferences, on_delete=models.CASCADE)
    tour_guide_preferences = models.OneToOneField(TourGuidePreferences, on_delete=models.CASCADE)
    paperwork_assistance = models.OneToOneField(PaperworkAssistance, on_delete=models.CASCADE)
    extra_requests = models.OneToOneField(ExtraRequests, on_delete=models.CASCADE)

    # Event organizer and vendor preferences
    vendors = models.ManyToManyField(Vendor, blank=True)  # Multiple vendors can be selected
    catering_or_chef = models.ForeignKey(CateringOrChef, on_delete=models.SET_NULL, null=True, blank=True)


    # Confirmation and Status fields
    confirmed = models.BooleanField(default=False)  # To track whether the itinerary is confirmed
    status = models.CharField(max_length=100, default="Pending", choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ])  # To track the current status of the itinerary
    notes = models.TextField(blank=True, null=True)  # Additional notes that can be added

    # Time fields for itinerary tracking
    created_at = models.DateTimeField(auto_now_add=True)  # Time of creation
    updated_at = models.DateTimeField(auto_now=True)  # Time of last update

    def __str__(self):
        return f"Itinerary for {self.user.username} - {self.journey_preferences.name}"

    class Meta:
        ordering = ['-created_at']  # Ordering by the most recent itinerary first

