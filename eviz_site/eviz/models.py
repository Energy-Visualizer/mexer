from django.db import models


class Dataset(models.Model):
    DatasetID = models.PositiveSmallIntegerField(primary_key=True)
    Dataset = models.TextField()
    class Meta:
        db_table = "Dataset"
class Country(models.Model):
    CountryID = models.PositiveSmallIntegerField(primary_key=True)
    Country = models.TextField()
    class Meta:
        db_table = "Country"

class Method(models.Model):
    MethodID = models.PositiveSmallIntegerField(primary_key=True)
    Method = models.TextField()
    class Meta:
        db_table = "Method"
    
class EnergyType(models.Model):
    EnergyTypeID = models.PositiveSmallIntegerField(primary_key=True)
    EnergyType = models.TextField()
    class Meta:
        db_table = "EnergyType"

class LastStage(models.Model):
    ECCStageID = models.PositiveSmallIntegerField(primary_key=True)
    ECCStage = models.TextField()
    class Meta:
        db_table = "ECCStage"
    
class IEAMW(models.Model):
    IEAMWID = models.PositiveSmallIntegerField(primary_key=True)
    IEAMW = models.TextField()
    class Meta:
        db_table = "IEAMW"
        
class IEAMW(models.Model):
    IEAMWID = models.PositiveSmallIntegerField(primary_key=True)
    IEAMW = models.TextField()
    class Meta:
        db_table = "IEAMW"

class IncludesNEU(models.Model):
    IncludesNEUID = models.PositiveSmallIntegerField(primary_key=True)
    IncludesNEU = models.BooleanField()
    class Meta:
        db_table = "IncludesNEU"

class Year(models.Model):
    YearID = models.PositiveSmallIntegerField(primary_key=True)
    Year = models.PositiveSmallIntegerField()
    class Meta:
        db_table = "Year"

class matname(models.Model):
    matnameID = models.PositiveSmallIntegerField(primary_key=True)
    matname = models.TextField()
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
        db_table = "PSUT"

        # TODO: for migration only?
        # managed = False # to use dataset as primary key

    Dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, db_column='Dataset') # primary_key=True
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='Country')
    Method = models.ForeignKey(Method, on_delete=models.CASCADE, db_column='Method')
    EnergyType = models.ForeignKey(EnergyType, on_delete=models.CASCADE, db_column='EnergyType')
    LastStage = models.ForeignKey(LastStage, on_delete=models.CASCADE, db_column='LastStage')
    IEAMW = models.ForeignKey(IEAMW, on_delete=models.CASCADE, db_column='IEAMW')
    IncludesNEU = models.ForeignKey(IncludesNEU, on_delete=models.CASCADE, db_column='IncludesNEU')
    Year = models.ForeignKey(Year, on_delete=models.CASCADE, db_column='Year')
    matname = models.ForeignKey(matname, on_delete=models.CASCADE, db_column='matname')
    i = models.OneToOneField(Index, on_delete=models.CASCADE, db_column='i')
    j = models.OneToOneField(Index, on_delete=models.CASCADE, db_column='j', related_name='j')
    x = models.FloatField()