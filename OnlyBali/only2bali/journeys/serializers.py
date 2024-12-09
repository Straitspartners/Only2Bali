from rest_framework import serializers
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

class JourneyPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JourneyPreferences
        fields = '__all__'

class PlacesToVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacesToVisit
        fields = '__all__'

class TravelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelDetails
        fields = '__all__'

class StayPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayPreferences
        fields = '__all__'

class FoodPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPreferences
        fields = '__all__'

class VehiclePreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePreferences
        fields = '__all__'

class TourGuidePreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuidePreferences
        fields = '__all__'

class CateringOrChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = CateringOrChef
        fields = '__all__'

class PaperworkAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperworkAssistance
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ExtraRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraRequests
        fields = '__all__'
