from django.db import models

# Create your models here.

class customer_detail(models.Model):
    occupant_name = models.CharField(max_length=10000)
    occupant_email = models.EmailField()
    occupant_occupation = models.CharField(max_length=10000)
    room_number = models.IntegerField()
    amount_paid = models.IntegerField()
    number_of_night = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.occupant_name



