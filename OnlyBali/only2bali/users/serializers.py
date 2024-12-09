from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving user data."""
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'mobile_number', 'is_verified']

class RegistrationSerializer(serializers.Serializer):
    """Serializer for validating user registration details."""
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    mobile_number = serializers.CharField(max_length=15)

    def validate(self, data):
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use."})
    
        if CustomUser.objects.filter(mobile_number=data['mobile_number']).exists():
            raise serializers.ValidationError({"mobile_number": "Mobile number is already registered."})

        return data


class OTPVerificationSerializer(serializers.Serializer):
    """Serializer for verifying OTP and creating user."""
    mobile_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        """Verify OTP and retrieve user data from cache."""
        mobile_number = data.get("mobile_number")
        otp = data.get("otp")
        cache_key = f"otp_{mobile_number}"

        # Retrieve data from cache
        user_data = cache.get(cache_key)
        if not user_data:
            raise serializers.ValidationError("OTP expired or invalid.")
        
        if user_data.get("otp") != otp:
            raise serializers.ValidationError("Invalid OTP.")

        return user_data

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("The old password is incorrect.")
        return value

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
    
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account found with this email.")
        return value

    def save(self):
        user = CustomUser.objects.get(email=self.validated_data['email'])
        otp = get_random_string(length=6, allowed_chars='0123456789')  # Generate OTP
        cache.set(user.email, otp, timeout=300)  # Store OTP for 5 minutes
        # Example: Send OTP via email
        send_mail(
            subject="Password Reset OTP",
            message=f"Your OTP is: {otp}",
            from_email="noreply@example.com",
            recipient_list=[user.email],
        )
        return {"email": user.email, "otp_sent": True}
    
class PasswordResetVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, data):
        cached_otp = cache.get(data['email'])
        if not cached_otp:
            raise serializers.ValidationError("OTP has expired or is invalid.")
        if cached_otp != data['otp']:
            raise serializers.ValidationError("Invalid OTP.")
        return data

    def save(self):
        user = CustomUser.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


# CustomUserSerializer

# For retrieving user details (e.g., profile, listing users).
# Includes all fields like id, username, email, mobile_number, and is_verified.

# RegistrationSerializer

# Validates the input during registration (username, email, password, mobile number).
# Ensures that the email and mobile number are unique.

# OTPVerificationSerializer

# Verifies the OTP provided by the user.
# If OTP is valid, the serializer returns the temporarily stored user details for creating the user in the database.
