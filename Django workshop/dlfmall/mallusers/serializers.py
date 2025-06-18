from rest_framework import serializers
class userDetailsSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    mobile = serializers.IntegerField()
    password = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50, allow_blank=True)
class membershipDetailsSerializers(serializers.Serializer):
    email = serializers.EmailField()
    membership_type = serializers.CharField(max_length=50)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
class eventDetailsSerializers(serializers.Serializer):
    email = serializers.EmailField()
    event_name = serializers.CharField(max_length=100)
    event_date = serializers.DateField()
    location = serializers.CharField(max_length=100)
class registrationDetailsSerializers(serializers.Serializer):
    email = serializers.EmailField()
    course_name = serializers.CharField(max_length=100)
    registration_date = serializers.DateField()
    status = serializers.CharField(max_length=50)
