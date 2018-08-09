from django.db import models
from datetime import datetime
#from django.core.url



class Table(models.Model):
    # id not needed as it is implicitly added
    name = models.CharField(max_length=250)
    details = models.TextField()


class Notices(Table):
    urgency_level = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "notices"

class Complaints(Table):
    urgency_level = models.CharField(max_length=20)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '-' + str(self.status)

    class Meta:
        verbose_name_plural = "complaints"

class Events(Table):
    event_date = models.DateField()
    budget = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "events"

class Staff(models.Model):
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)

    def __str__(self):
        return self.name + '-' + self.job
    class Meta:
        verbose_name_plural = "staff"

class Attendance(models.Model):
    present = models.BooleanField()
    date = models.DateField()
    staff = models.ForeignKey(Staff)

    def __str__(self):
        return str(self.present) + '-' + self.staff.name
    class Meta:
        verbose_name_plural = "attendance"

