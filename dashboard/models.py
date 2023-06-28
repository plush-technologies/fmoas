from django.db import models
from datetime import datetime

# Create your models here.

# The type list containing priority levels e.g. low medium high
class PriorityType(models.Model):
    priority = models.CharField(max_length=50)


# The type list containing various sensor types e.g. IR, load detector, sonar....
# TODO - check the value data type is sufficient for the data comming in from the database
class SensorType(models.Model):
    dateTimeRecorded = models.DateTimeField(default=datetime.now, blank=True)
    value = models.IntegerField()

# Holds each particular sensor and stores the sensor type of that sensor. This is then
# referenced by the SensorData table to know what data is coming from what sensor.
class Sensor(models.Model):
    sensorType = models.ForeignKey(SensorType, on_delete=models.CASCADE)

# Table which will hold the data coming in from sensors.
class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    # value

# The type list containing the various types of facilities.
# TODO - there may be more fields required!
class FacilityType(models.Model):
    facilityType = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)

# Type list containing values for the facility status e.g. out of order, occupied, available etc 
class FacilityStatus(models.Model):
    FacilityStatus = models.CharField(max_length=50)

# Location data for a specific facility
class Location(models.Model):
    gps = models.IntegerField # TODO check how gps is stored - probably 1 lat field one long field
    buildingName = models.CharField(max_length=100)
    buildingNumber = models.IntegerField()
    level = models.IntegerField()
    room = models.IntegerField()

# Table containing all the important information about a particular facility
class Facility(models.Model):
    name = models.CharField(max_length=150)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    facilityType = models.ForeignKey(FacilityType, on_delete=models.CASCADE)
    status = models.ForeignKey(FacilityStatus, on_delete=models.CASCADE)
    stall = models.IntegerField() # if not toilet type then 0 else increment starting from 1 for each toilet

# Staff levels e.g. Admin, Maintenance ...
class StaffLevel(models.Model):
    staffLevel = models.CharField(max_length=50) 

# The different types of skills a staff member could have e.g. plumming electrical ...
class SkillType(models.Model):
    skillType = models.CharField(max_length=50)

# Staff member information
class Staff(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    department = models.CharField(max_length=50) # from Ang don't know exactly what he wanted us to put here
    level = models.ForeignKey(StaffLevel, on_delete=models.CASCADE)
    skillType = models.ForeignKey(SkillType, on_delete=models.CASCADE)

class Task(models.Model):
    dateAssigned = models.DateTimeField(default=datetime.now, blank=True)
    textDescription = models.TextField()
    staffComment = models.TextField() # TODO: need some way to specify blanks
    priority = models.ForeignKey(PriorityType, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    staffMember = models.ForeignKey(Staff, on_delete=models.CASCADE)
    # image

class CompletedTask(models.Model):
    dateCompleted = models.DateTimeField(default=datetime.now, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)




