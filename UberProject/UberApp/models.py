from django.db import models

class Uber(models.Model):
    DBP = models.IntegerField()
    DAP = models.IntegerField()
    TMF = models.IntegerField()
    Distance = models.IntegerField()