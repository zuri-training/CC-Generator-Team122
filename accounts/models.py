from django.db import models

# Create your models here.
# name, card no, exp date, cvv no.abs

class card(models.Model):
    name = models.CharField(max_length=100)
    card_no = models.IntegerField()
    exp_date = models.IntegerField()
    cvv_no = models.IntegerField()
    
