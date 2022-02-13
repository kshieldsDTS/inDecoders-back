from django.db import models

# Create your models here.
class LFWork(models.Model):
    owner = models.ForeignKey(
        'users.User', related_name='LFWorkowner', on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    skills = models.CharField(max_length=500, blank=True)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    availability = models.CharField(max_length=100, blank=True)
    payrate_desired = models.IntegerField(default=0)
    
    def __str__(self):
        return self.owner

class LFHelp(models.Model):
    owner = models.ForeignKey(
        'users.User', related_name='LFHelp', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    contact = models.CharField(max_length=500, default=owner)
    skills_desired = models.CharField(max_length=500, blank=True)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    availability_desired = models.CharField(max_length=100, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    payrate = models.IntegerField(default=0)
    def __str__(self):
        return self.owner