from django.db import models


class carEntry(models.Model):
    number_plate = models.CharField(max_length=200)
    enter_date = models.DateTimeField()

    def __str__(self):
        return self.number_plate


class carExit(models.Model):
    number_plate = models.CharField(max_length=200)
    exit_date = models.DateTimeField('date published')

class carDetails(models.Model):
    car_driver = models.CharField(max_length=200)
    driver_rating = models.FloatField(default=0.0)
    driver_review = models.CharField(max_length=200)
    driver_contact= models.IntegerField(default=0)
    car_number=models.CharField(max_length=20,default=0)

    def __str__(self):
        return self.car_number

class Test(models.Model):
    number=models.CharField(max_length=200)

    def __str__(self):
        return self.number



