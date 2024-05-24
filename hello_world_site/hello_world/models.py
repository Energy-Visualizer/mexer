from django.db import models

class PSUT(models.Model):
    dataset = models.PositiveSmallIntegerField()
    country = models.PositiveSmallIntegerField()
    method = models.PositiveSmallIntegerField()
    energy_type = models.PositiveSmallIntegerField()
    last_stange = models.PositiveSmallIntegerField()
    ieamw = models.PositiveSmallIntegerField()
    includes_neu = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    mat_name = models.PositiveSmallIntegerField()
    i = models.PositiveSmallIntegerField()
    j = models.PositiveSmallIntegerField()
    x = models.FloatField()