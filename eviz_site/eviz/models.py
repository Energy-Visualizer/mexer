from django.db import models

class PSUT(models.Model):

    # define meta attributes
    class Meta:
        db_table = "PSUT"

    Dataset = models.PositiveSmallIntegerField()
    Country = models.PositiveSmallIntegerField()
    Method = models.PositiveSmallIntegerField()
    EnergyType = models.PositiveSmallIntegerField()
    LastStage = models.PositiveSmallIntegerField()
    IEAMW = models.PositiveSmallIntegerField()
    IncludesNEU = models.PositiveSmallIntegerField()
    Year = models.PositiveSmallIntegerField()
    matname = models.PositiveSmallIntegerField()
    i = models.PositiveSmallIntegerField()
    j = models.PositiveSmallIntegerField()
    x = models.FloatField()

class Index(models.Model):

    class Meta:
        db_table = "Index"
    
    IndexID = models.PositiveSmallIntegerField()
    Index = models.TextField()