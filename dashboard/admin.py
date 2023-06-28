from django.contrib import admin
from .models import PriorityType, SensorType, Sensor, SensorData, FacilityType, FacilityStatus, Location, Facility, StaffLevel, SkillType, Staff, Task, CompletedTask

# Register your models here.
admin.site.register(PriorityType)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(SensorData)
admin.site.register(FacilityType)
admin.site.register(FacilityStatus)
admin.site.register(Location)
admin.site.register(Facility)
admin.site.register(StaffLevel)
admin.site.register(SkillType)
admin.site.register(Staff)
admin.site.register(Task)
admin.site.register(CompletedTask)
