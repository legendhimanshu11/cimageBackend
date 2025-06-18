from django.db import models

class userDetails(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(primary_key=True)
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True,blank=True)
membershipName = (("Silver","Silver"),
                  ("Gold","Gold"),
                  ("Platinum","Platinum")
                  )
class membershipDetails(models.Model):
    membershipCategory = models.CharField(max_length=20,choices=membershipName)
    membershipID = models.CharField(primary_key=True,max_length=50)
    email = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    validity = models.DateField()
class eventDetails(models.Model):
    eventID = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50,unique=True)
    eventDescription = models.CharField(max_length=100)
    eventDate = models.DateField()
    eventVenue = models.CharField(max_length=50)
    user = models.ForeignKey(userDetails, on_delete=models.CASCADE)
class registrationDetails(models.Model):
    registrationID = models.AutoField(primary_key=True)
    eventID = models.ForeignKey(eventDetails, on_delete=models.CASCADE)
    email = models.ForeignKey(userDetails, on_delete=models.CASCADE)
