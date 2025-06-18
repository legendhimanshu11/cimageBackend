from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .models import *

class usersSignup(APIView):
    def post(self,request):
        serializersData = userDetailsSerializers(data = request.data)
        if serializersData.is_valid():
            userDetails.objects.create(**serializersData.data)
            message = {"message":"User Signup Successfully"}
            return JsonResponse(message)
        return JsonResponse(serializersData.errors)
class userMembership(APIView):
    def get(self,request,email):
        result = list(membershipDetails.objects.filter(email=email).values())
        message = {"Membership Details":result}
        return JsonResponse(message,safe=False)
class EventDetailsView(APIView):
    def get(self,request,email):
        result = list(eventDetails.objects.filter(email=email).values())
        message = {"Event Details":result}
        return JsonResponse(message,safe=False)
class registrationDetails(APIView):
    def get(self,request,email):
        result = list(registrationDetails.objects.filter(email=email).values())
        message = {"Registration Details":result}
        return JsonResponse(message,safe=False)
