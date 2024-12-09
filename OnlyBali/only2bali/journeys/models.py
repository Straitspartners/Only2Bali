from django.db import models
from users.models import CustomUser

# 5 . Then we have to select about our crew like Business Partners , 
# Corporate meeting , Team Bonding , Alumini Meeting , Friends Get - Together ,
# Family , New Couple , Family get - together and there will also be others option 
# if we dont find our options here then we can type about it in others.

class JourneyPreferences(models.Model):
    CREW_TYPE_CHOICES = [
        ('business_partners', 'Business Partners'),
        ('corporate_meeting', 'Corporate Meeting'),
        ('team_bonding', 'Team Bonding'),
        ('alumni_meeting', 'Alumni Meeting'),
        ('friends_get_together', 'Friends Get-Together'),
        ('family', 'Family'),
        ('new_couple', 'New Couple'),
        ('family_get_together', 'Family Get-Together'),
        ('others', 'Others'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=150)
    times_visited_bali = models.IntegerField(default=0)
    crew_type = models.CharField(max_length=50, choices=CREW_TYPE_CHOICES)
    crew_type_others = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.name}'s Journey Preferences"

# 6 . Then we can select which are all the places we wanted to visit in Bali 
# like Natural Beauty and Beaches , Local Cultures and Traditions , Wellness and 
# Relaxation , Wedding and Pre-Wedding , Adventures and Activities , Local Culinary ,
# Shopping in Bali , Luxury and Unique Experiences 

class PlacesToVisit(models.Model):
    PLACES_CHOICES = [
        ('natural_beauty', 'Natural Beauty and Beaches'),
        ('local_culture', 'Local Cultures and Traditions'),
        ('wellness_relaxation', 'Wellness and Relaxation'),
        ('wedding_pre_wedding', 'Wedding and Pre-Wedding'),
        ('adventures_activities', 'Adventures and Activities'),
        ('local_culinary', 'Local Culinary'),
        ('shopping', 'Shopping in Bali'),
        ('luxury_experiences', 'Luxury and Unique Experiences'),
        ('others', 'Others'),
    ]

    journey_preferences = models.ForeignKey(JourneyPreferences, on_delete=models.CASCADE)
    place = models.CharField(max_length=50, choices=PLACES_CHOICES)
    others_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.place} for {self.journey_preferences.name}"

# 7 . Then in the next page , the user will enter the Departure Date and Time , Arrival Date and Time ,
# International Airport , Preferred Flight Class 

class TravelDetails(models.Model):
    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    international_airport = models.CharField(max_length=100)
    flight_class = models.CharField(max_length=50)

    def __str__(self):
        return f"Travel Details for {self.journey_preferences.name}"

# 8 . In the next page the user can select the type of stay like hotel,motel,villa,cottages,appartment and guesthouse

class StayPreferences(models.Model):
    STAY_TYPE_CHOICES = [
        ('hotel', 'Hotel'),
        ('motel', 'Motel'),
        ('villa', 'Villa'),
        ('cottage', 'Cottage'),
        ('apartment', 'Apartment'),
        ('guesthouse', 'Guesthouse'),
    ]

    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    stay_type = models.CharField(max_length=50, choices=STAY_TYPE_CHOICES)

    def __str__(self):
        return f"{self.stay_type} for {self.journey_preferences.name}"

# 9 . Then they can select the foods they need IN Vegetarain There will be North Indian Vegetarian , South Indian Vegetarain ,
# Gujarati Vegetarain , Jain Vegetarian and IN Non Vegetarain There will be North Indian Non-Vegetarian , South Indian Non-Vegetarain ,
# IN Other Dietry there will be Vegan , Keto , Halal and IN Balinese Dish Preferences there will be Jimbaran SeaFood , Balinese Culinary,
# Indonesian Food , Local Snacks , Souvenir Foods and in others we can type if dont find our preferences.	

class FoodPreferences(models.Model):
    # Vegetarian preferences
    VEGETARIAN_CHOICES = [
        ('north_indian', 'North Indian Vegetarian'),
        ('south_indian', 'South Indian Vegetarian'),
        ('gujarati', 'Gujarati Vegetarian'),
        ('jain', 'Jain Vegetarian')
    ]
    
    # Non-Vegetarian preferences
    NON_VEGETARIAN_CHOICES = [
        ('north_indian', 'North Indian Non-Vegetarian'),
        ('south_indian', 'South Indian Non-Vegetarian')
    ]
    
    # Other dietary preferences
    DIETARY_CHOICES = [
        ('vegan', 'Vegan'),
        ('keto', 'Keto'),
        ('halal', 'Halal')
    ]
    
    # Balinese dish preferences
    BALINESE_CHOICES = [
        ('jimbaran_seafood', 'Jimbaran Seafood'),
        ('balinese_culinary', 'Balinese Culinary'),
        ('indonesian_food', 'Indonesian Food'),
        ('local_snacks', 'Local Snacks'),
        ('souvenir_foods', 'Souvenir Foods')
    ]

    # Fields to store user selections
    vegetarian_choice = models.CharField(max_length=50, choices=VEGETARIAN_CHOICES, blank=True, null=True)
    non_vegetarian_choice = models.CharField(max_length=50, choices=NON_VEGETARIAN_CHOICES, blank=True, null=True)
    dietary_choice = models.CharField(max_length=50, choices=DIETARY_CHOICES, blank=True, null=True)
    balinese_choice = models.CharField(max_length=50, choices=BALINESE_CHOICES, blank=True, null=True)
    other_preferences = models.TextField(blank=True, null=True)  # For additional dietary preferences if 'other' is chosen

    def __str__(self):
        preferences = []
        if self.vegetarian_choice:
            preferences.append(f"Vegetarian: {self.vegetarian_choice}")
        if self.non_vegetarian_choice:
            preferences.append(f"Non-Vegetarian: {self.non_vegetarian_choice}")
        if self.dietary_choice:
            preferences.append(f"Dietary: {self.dietary_choice}")
        if self.balinese_choice:
            preferences.append(f"Balinese Dish: {self.balinese_choice}")
        if self.other_preferences:
            preferences.append(f"Other Preferences: {self.other_preferences}")
        
        return ', '.join(preferences)


# 10 . Then in the next page we can select the Type of Vehicle like Motorbike ( 1-2 people ), Bus (>30 people) ,
# MiniBus (20-30 people) , Van (12-15 people) , Car (5-10 people ) , Luxury Car (5-8 people) and in the same page 
# we have Rent Period like 1-2 Days , >3 Days and we have others option to type something and we can choose 
# Include Driver ? Yes , No

class VehiclePreferences(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('motorbike', 'Motorbike (1-2 people)'),
        ('bus', 'Bus (>30 people)'),
        ('minibus', 'MiniBus (20-30 people)'),
        ('van', 'Van (12-15 people)'),
        ('car', 'Car (5-10 people)'),
        ('luxury_car', 'Luxury Car (5-8 people)'),
    ]

    RENT_PERIOD_CHOICES = [
        ('1_2_days', '1-2 Days'),
        ('more_than_3_days', '>3 Days'),
    ]

    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPE_CHOICES)
    rent_period = models.CharField(max_length=20, choices=RENT_PERIOD_CHOICES)
    include_driver = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle_type} for {self.journey_preferences.name}"

# 11 . In the next page we have I prefer a Tour Guide Who Speaks like Tamil , Englsih , Hindi , Marathi , 
# Gujarati and Kannada and in others we can type something 

class TourGuidePreferences(models.Model):
    LANGUAGES_CHOICES = [
        ('tamil', 'Tamil'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('marathi', 'Marathi'),
        ('gujarati', 'Gujarati'),
        ('kannada', 'Kannada'),
        ('others', 'Others'),
    ]

    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    preferred_language = models.CharField(max_length=50, choices=LANGUAGES_CHOICES)
    other_language = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Tour Guide Preferences for {self.journey_preferences.name}"

# 12 . In the next page we can select whether we want Personal Chef or Catering .	

class CateringOrChef(models.Model):
    SERVICE_CHOICES = [
        ('personal_chef', 'Personal Chef'),
        ('catering', 'Catering'),
        ('other', 'Other')
    ]
    
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True, null=True)  # User can describe their specific need if 'Other' is selected

    def __str__(self):
        return self.service_type

# 13 . In the next page we have Paperwork like KYC Integration , Visa Processing Assistance and 
# Travel Requirement guidance and there is a option for others We can type something there .

class PaperworkAssistance(models.Model):
    ASSISTANCE_CHOICES = [
        ('kyc_integration', 'KYC Integration'),
        ('visa_processing', 'Visa Processing Assistance'),
        ('travel_requirements', 'Travel Requirement Guidance'),
        ('others', 'Others'),
    ]

    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    assistance_type = models.CharField(max_length=50, choices=ASSISTANCE_CHOICES)
    other_assistance_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Paperwork Assistance for {self.journey_preferences.name}"

# 14 . In the next page we can select like Event Organizer , Vegetable Vendors , Utensil Vendors , Travel Agent 
# and there will also be others option if we dont find our options here then we can type about it in others.		

class Vendor(models.Model):
    VENDOR_CHOICES = [
        ('vegetable', 'Vegetable Vendor'),
        ('utensil', 'Utensil Vendor'),
        ('travel_agent', 'Travel Agent'),
        ('event_organizer', 'Event Organizer'),  
        ('other', 'Other')
    ]
    
    vendor_type = models.CharField(max_length=20, choices=VENDOR_CHOICES, default='other')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.vendor_type}: {self.name}"

# 15 . And at the final , there will be a request box there the user can type any extra information they need   

class ExtraRequests(models.Model):
    journey_preferences = models.OneToOneField(JourneyPreferences, on_delete=models.CASCADE)
    requests = models.TextField()

    def __str__(self):
        return f"Extra Requests for {self.journey_preferences.name}"
