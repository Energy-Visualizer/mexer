from django.db import models

class PSUT(models.Model):

    # define meta attributes
    class Meta:
        db_table = "PSUT"

        # TODO: for migration only?
        # managed = False # to use dataset as primary key

    Dataset = models.PositiveSmallIntegerField() # primary_key=True
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