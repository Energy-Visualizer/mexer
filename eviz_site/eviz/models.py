from django.db import models


class Dataset(models.Model):
    DatasetID = models.PositiveSmallIntegerField(primary_key=True)
    Dataset = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "Dataset"
class Country(models.Model):
    CountryID = models.PositiveSmallIntegerField(primary_key=True)
    Country = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    IsCountry = models.BooleanField()
    IsAggregation = models.BooleanField()
    IsContinent = models.BooleanField()
    class Meta:
        db_table = "Country"

class Method(models.Model):
    MethodID = models.PositiveSmallIntegerField(primary_key=True)
    Method = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "Method"
    
class EnergyType(models.Model):
    EnergyTypeID = models.PositiveSmallIntegerField(primary_key=True)
    EnergyType = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "EnergyType"

class LastStage(models.Model):
    ECCStageID = models.PositiveSmallIntegerField(primary_key=True)
    ECCStage = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "ECCStage"
    
class IEAMW(models.Model):
    IEAMWID = models.PositiveSmallIntegerField(primary_key=True)
    IEAMW = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "IEAMW"

class IncludesNEU(models.Model):
    IncludesNEUID = models.PositiveSmallIntegerField(primary_key=True)
    IncludesNEU = models.BooleanField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "IncludesNEU"

class Year(models.Model):
    YearID = models.PositiveSmallIntegerField(primary_key=True)
    Year = models.PositiveSmallIntegerField()
    class Meta:
        db_table = "Year"
        
class AggLevel(models.Model):
    AggLevelID = models.PositiveSmallIntegerField(primary_key=True)
    AggLevel = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "AggLevel"

class matname(models.Model):
    matnameID = models.PositiveSmallIntegerField(primary_key=True)
    matname = models.TextField()
    FullName = models.TextField()
    Description = models.TextField()
    class Meta:
        db_table = "matname"

        
class Index(models.Model):
    IndexID = models.PositiveSmallIntegerField(primary_key=True)
    Index = models.TextField()
    class Meta:
        db_table = "Index"
        

class PSUT(models.Model):

    # define meta attributes
    class Meta:
        db_table = "PSUTReAllChopAllDsAllGrAll"

    Dataset = models.PositiveSmallIntegerField()
    Country = models.PositiveSmallIntegerField()
    Method = models.PositiveSmallIntegerField()
    EnergyType = models.PositiveSmallIntegerField()
    LastStage = models.PositiveSmallIntegerField()
    IEAMW = models.PositiveSmallIntegerField()
    IncludesNEU = models.PositiveSmallIntegerField()
    Year = models.PositiveSmallIntegerField()
    ChoppedMat = models.PositiveSmallIntegerField()
    ChoppedVar = models.PositiveSmallIntegerField()
    ProductAggregation = models.PositiveSmallIntegerField()
    IndustryAggregation = models.PositiveSmallIntegerField()
    matname = models.PositiveSmallIntegerField()
    i = models.PositiveSmallIntegerField()
    j = models.PositiveSmallIntegerField()
    x = models.FloatField()