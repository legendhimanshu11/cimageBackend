from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.usersSignup.as_view()),
    path("getMembershipDetails/<email>/",views.userMembership.as_view()),
    path("getEventDetails/<email>/",views.EventDetailsView.as_view()),
    path("getRegistrationDetails/<email>/",views.registrationDetails.as_view())
]