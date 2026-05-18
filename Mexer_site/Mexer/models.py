from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.db.models.deletion import CASCADE


class EvizUser(DjangoUser):
    """Model representing a database table named 'EvizUser'."""

    institution_type = models.CharField(
        max_length=10,
        default="Other",
        choices={
            "Academic": "Academic",
            "Government": "Government",
            "Industry": "Industry",
            "Non-Profit": "Non-Profit",
            "Other": "Other",
        },
    )
    institution_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class EmailAuthCode(models.Model):
    """Model for storing email auhtentication codes and associated account information."""

    code = models.TextField(max_length=255, primary_key=True)
    account = models.ForeignKey(to=EvizUser, on_delete=CASCADE)


class PassResetCode(models.Model):
    """Model for storing password reset codes and the associated user."""

    code = models.TextField(max_length=255, primary_key=True)
    user = models.ForeignKey(EvizUser, on_delete=models.CASCADE)


class Papers(models.Model):
    """Model for the 'Papers' database table.'"""

    class Meta:
        db_table = "Papers"
        managed = False

    papers_id = models.IntegerField(db_column="PapersID", primary_key=True)
    authors = models.TextField(db_column="Authors")
    year = models.IntegerField(db_column="Year")
    title = models.TextField(db_column="Title")
    journal = models.TextField(db_column="Journal")
    volume = models.TextField(db_column="Volume")
    number = models.TextField(db_column="Number")
    pages = models.TextField(db_column="Pages")
    doi = models.TextField(db_column="doi")
    url = models.TextField(db_column="URL")


class Dataset(models.Model):
    """Model for the 'Dataset' database table.'"""

    class Meta:
        db_table = "Dataset"
        managed = False

    dataset_id = models.IntegerField(db_column="DatasetID", primary_key=True)
    dataset = models.TextField(db_column="Dataset")
    public = models.BooleanField(db_column="Public")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class Version(models.Model):
    """Model for the 'Version' database table.'"""

    class Meta:
        db_table = "Version"
        managed = False

    version_id = models.IntegerField(db_column="VersionID", primary_key=True)
    version = models.TextField(db_column="Version")
    release_date = models.TextField(db_column="ReleaseDate")
    public = models.BooleanField(db_column="Public")
    change_notes = models.TextField(db_column="ChangeNotes")


class Country(models.Model):
    """Model for the 'Country' database table.'"""

    class Meta:
        db_table = "Country"
        managed = False

    country_id = models.IntegerField(db_column="CountryID", primary_key=True)
    country = models.TextField(db_column="Country")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")
    is_country = models.BooleanField(db_column="IsCountry")
    is_canonical_country = models.BooleanField(db_column="IsCanonicalCountry")
    is_aggregation = models.BooleanField(db_column="IsAggregation")
    is_continent = models.BooleanField(db_column="IsContinent")


class Year(models.Model):
    """Model for the 'Year' database table.'"""

    class Meta:
        db_table = "Year"
        managed = False

    year_id = models.IntegerField(db_column="YearID", primary_key=True)
    year = models.IntegerField(db_column="Year")


class Method(models.Model):
    """Model for the 'Method' database table.'"""

    class Meta:
        db_table = "Method"
        managed = False

    method_id = models.IntegerField(db_column="MethodID", primary_key=True)
    method = models.TextField(db_column="Method")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class EnergyType(models.Model):
    """Model for the 'EnergyType' database table.'"""

    class Meta:
        db_table = "EnergyType"
        managed = False

    energy_type_id = models.IntegerField(db_column="EnergyTypeID", primary_key=True)
    energy_type = models.TextField(db_column="EnergyType")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class ECCStage(models.Model):
    """Model for the 'ECCStage' database table.'"""

    class Meta:
        db_table = "ECCStage"
        managed = False

    ecc_stage_id = models.IntegerField(db_column="ECCStageID", primary_key=True)
    ecc_stage = models.TextField(db_column="ECCStage")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class IEALedgerSide(models.Model):
    """Model for the 'IEALedgerSide' database table.'"""

    class Meta:
        db_table = "IEALedgerSide"
        managed = False

    iea_ledger_side_id = models.IntegerField(
        db_column="IEALedgerSideID", primary_key=True
    )
    iea_ledger_side = models.TextField(db_column="IEALedgerSide")


class IEAFlowAggregationPoint(models.Model):
    """Model for the 'IEAFlowAggregationPoint' database table.'"""

    class Meta:
        db_table = "IEAFlowAggregationPoint"
        managed = False

    iea_flow_aggregation_point_id = models.IntegerField(
        db_column="IEAFlowAggregationPointID", primary_key=True
    )
    iea_flow_aggregation_point = models.TextField(db_column="IEAFlowAggregationPoint")


class Index(models.Model):
    """Model for the 'Index' database table.'"""

    class Meta:
        db_table = "Index"
        managed = False

    index_id = models.IntegerField(db_column="IndexID", primary_key=True)
    index = models.TextField(db_column="Index")
    order = models.IntegerField(db_column="Order")
    sankey_column = models.IntegerField(db_column="SankeyColumn")


class Unit(models.Model):
    """Model for the 'Unit' database table.'"""

    class Meta:
        db_table = "Unit"
        managed = False

    unit_id = models.IntegerField(db_column="UnitID", primary_key=True)
    unit = models.TextField(db_column="Unit")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class AggLevel(models.Model):
    """Model for the 'AggLevel' database table.'"""

    class Meta:
        db_table = "AggLevel"
        managed = False

    agg_level_id = models.IntegerField(db_column="AggLevelID", primary_key=True)
    agg_level = models.TextField(db_column="AggLevel")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class GrossNet(models.Model):
    """Model for the 'GrossNet' database table.'"""

    class Meta:
        db_table = "GrossNet"
        managed = False

    gross_net_id = models.IntegerField(db_column="GrossNetID", primary_key=True)
    gross_net = models.TextField(db_column="GrossNet")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class Matname(models.Model):
    """Model for the 'matname' database table.'"""

    class Meta:
        db_table = "matname"
        managed = False

    matname_id = models.IntegerField(db_column="matnameID", primary_key=True)
    matname = models.TextField(db_column="matname")
    full_name = models.TextField(db_column="FullName")
    public = models.BooleanField(db_column="Public")
    description = models.TextField(db_column="Description")
    row_format = models.TextField(db_column="RowFormat")
    col_format = models.TextField(db_column="ColFormat")


class IndProdType(models.Model):
    """Model for the 'IndProdType' database table.'"""

    class Meta:
        db_table = "IndProdType"
        managed = False

    ind_prod_type_id = models.IntegerField(db_column="IndProdTypeID", primary_key=True)
    ind_prod_type = models.TextField(db_column="IndProdType")


class RCType(models.Model):
    """Model for the 'RCType' database table.'"""

    class Meta:
        db_table = "RCType"
        managed = False

    rc_type_id = models.IntegerField(db_column="RCTypeID", primary_key=True)
    rc_type = models.TextField(db_column="RCType")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class IncludesNEU(models.Model):
    """Model for the 'IncludesNEU' database table.'"""

    class Meta:
        db_table = "IncludesNEU"
        managed = False

    includes_neuid = models.IntegerField(db_column="IncludesNEUID", primary_key=True)
    includes_neu = models.BooleanField(db_column="IncludesNEU")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class Quantity(models.Model):
    """Model for the 'Quantity' database table.'"""

    class Meta:
        db_table = "Quantity"
        managed = False

    quantity_id = models.IntegerField(db_column="QuantityID", primary_key=True)
    quantity = models.TextField(db_column="Quantity")


class Species(models.Model):
    """Model for the 'Species' database table.'"""

    class Meta:
        db_table = "Species"
        managed = False

    species_id = models.IntegerField(db_column="SpeciesID", primary_key=True)
    species = models.TextField(db_column="Species")


class PhiSource(models.Model):
    """Model for the 'PhiSource' database table.'"""

    class Meta:
        db_table = "PhiSource"
        managed = False

    phi_source_id = models.IntegerField(db_column="PhiSourceID", primary_key=True)
    phi_source = models.TextField(db_column="PhiSource")


class MatnameRCType(models.Model):
    """Model for the 'matnameRCType' database table.'"""

    class Meta:
        db_table = "matnameRCType"
        managed = False

    matname = models.IntegerField(db_column="matname", primary_key=True)
    rowtype = models.IntegerField(db_column="rowtype")
    coltype = models.IntegerField(db_column="coltype")


class AllIEAData(models.Model):
    """Model for the 'AllIEAData' database table.'"""

    class Meta:
        db_table = "AllIEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    ledger_side = models.IntegerField(db_column="LedgerSide", primary_key=True)
    flow_aggregation_point = models.IntegerField(
        db_column="FlowAggregationPoint", primary_key=True
    )
    flow = models.IntegerField(db_column="Flow", primary_key=True)
    product = models.IntegerField(db_column="Product", primary_key=True)
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")


class IEAData(models.Model):
    """Model for the 'IEAData' database table.'"""

    class Meta:
        db_table = "IEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    ledger_side = models.IntegerField(db_column="LedgerSide", primary_key=True)
    flow_aggregation_point = models.IntegerField(
        db_column="FlowAggregationPoint", primary_key=True
    )
    flow = models.IntegerField(db_column="Flow", primary_key=True)
    product = models.IntegerField(db_column="Product", primary_key=True)
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")


class BalancedIEAData(models.Model):
    """Model for the 'BalancedIEAData' database table.'"""

    class Meta:
        db_table = "BalancedIEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    ledger_side = models.IntegerField(db_column="LedgerSide", primary_key=True)
    flow_aggregation_point = models.IntegerField(
        db_column="FlowAggregationPoint", primary_key=True
    )
    flow = models.IntegerField(db_column="Flow", primary_key=True)
    product = models.IntegerField(db_column="Product", primary_key=True)
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")


class SpecifiedIEAData(models.Model):
    """Model for the 'SpecifiedIEAData' database table.'"""

    class Meta:
        db_table = "SpecifiedIEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    ledger_side = models.IntegerField(db_column="LedgerSide", primary_key=True)
    flow_aggregation_point = models.IntegerField(
        db_column="FlowAggregationPoint", primary_key=True
    )
    flow = models.IntegerField(db_column="Flow", primary_key=True)
    product = models.IntegerField(db_column="Product", primary_key=True)
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")


class AMWPFUDataRaw(models.Model):
    """Model for the 'AMWPFUDataRaw' database table.'"""

    class Meta:
        db_table = "AMWPFUDataRaw"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    species = models.IntegerField(db_column="Species", primary_key=True)
    stage = models.IntegerField(db_column="Stage", primary_key=True)
    sector = models.IntegerField(db_column="Sector", primary_key=True)
    unit = models.IntegerField(db_column="Unit", primary_key=True)
    edot = models.FloatField(db_column="Edot")


class AMWPFUData(models.Model):
    """Model for the 'AMWPFUData' database table.'"""

    class Meta:
        db_table = "AMWPFUData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    species = models.IntegerField(db_column="Species", primary_key=True)
    stage = models.IntegerField(db_column="Stage", primary_key=True)
    sector = models.IntegerField(db_column="Sector", primary_key=True)
    unit = models.IntegerField(db_column="Unit", primary_key=True)
    edot = models.FloatField(db_column="Edot")


class HMWPFUDataRaw(models.Model):
    """Model for the 'HMWPFUDataRaw' database table.'"""

    class Meta:
        db_table = "HMWPFUDataRaw"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    species = models.IntegerField(db_column="Species", primary_key=True)
    stage = models.IntegerField(db_column="Stage", primary_key=True)
    sector = models.IntegerField(db_column="Sector", primary_key=True)
    unit = models.IntegerField(db_column="Unit", primary_key=True)
    edot = models.FloatField(db_column="Edot")


class HMWPFUData(models.Model):
    """Model for the 'HMWPFUData' database table.'"""

    class Meta:
        db_table = "HMWPFUData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    species = models.IntegerField(db_column="Species", primary_key=True)
    stage = models.IntegerField(db_column="Stage", primary_key=True)
    sector = models.IntegerField(db_column="Sector", primary_key=True)
    unit = models.IntegerField(db_column="Unit", primary_key=True)
    edot = models.FloatField(db_column="Edot")


class IncompleteAllocationTables(models.Model):
    """Model for the 'IncompleteAllocationTables' database table.'"""

    class Meta:
        db_table = "IncompleteAllocationTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    ledger_side = models.IntegerField(db_column="LedgerSide", primary_key=True)
    flow_aggregation_point = models.IntegerField(
        db_column="FlowAggregationPoint", primary_key=True
    )
    ef_product = models.IntegerField(db_column="EfProduct", primary_key=True)
    machine = models.IntegerField(db_column="Machine", primary_key=True)
    eu_product = models.IntegerField(db_column="EuProduct", primary_key=True)
    destination = models.IntegerField(db_column="Destination", primary_key=True)
    quantity = models.IntegerField(db_column="Quantity", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    value = models.FloatField(db_column="Value")


class CompletedAllocationTables(models.Model):
    """Model for the 'CompletedAllocationTables' database table.'"""

    class Meta:
        db_table = "CompletedAllocationTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    ledger_side = models.IntegerField(db_column="LedgerSide", primary_key=True)
    flow_aggregation_point = models.IntegerField(
        db_column="FlowAggregationPoint", primary_key=True
    )
    ef_product = models.IntegerField(db_column="EfProduct", primary_key=True)
    machine = models.IntegerField(db_column="Machine", primary_key=True)
    eu_product = models.IntegerField(db_column="EuProduct", primary_key=True)
    destination = models.IntegerField(db_column="Destination", primary_key=True)
    quantity = models.IntegerField(db_column="Quantity", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    value = models.FloatField(db_column="Value")
    c_source = models.IntegerField(db_column="CSource", primary_key=True)


class Cmats(models.Model):
    """Model for the 'Cmats' database table.'"""

    class Meta:
        db_table = "Cmats"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class AllMachineData(models.Model):
    """Model for the 'AllMachineData' database table.'"""

    class Meta:
        db_table = "AllMachineData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    machine = models.IntegerField(db_column="Machine", primary_key=True)
    eu_product = models.IntegerField(db_column="EuProduct", primary_key=True)
    quantity = models.IntegerField(db_column="Quantity", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    value = models.FloatField(db_column="Value")


class MachineData(models.Model):
    """Model for the 'MachineData' database table.'"""

    class Meta:
        db_table = "MachineData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    machine = models.IntegerField(db_column="Machine", primary_key=True)
    eu_product = models.IntegerField(db_column="EuProduct", primary_key=True)
    quantity = models.IntegerField(db_column="Quantity", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    value = models.FloatField(db_column="Value")


class CompletedEfficiencyTables(models.Model):
    """Model for the 'CompletedEfficiencyTables' database table.'"""

    class Meta:
        db_table = "CompletedEfficiencyTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    machine = models.IntegerField(db_column="Machine", primary_key=True)
    eu_product = models.IntegerField(db_column="EuProduct", primary_key=True)
    quantity = models.IntegerField(db_column="Quantity", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    value = models.FloatField(db_column="Value")
    etafu_source = models.IntegerField(db_column="etafuSource", primary_key=True)


class PhiConstants(models.Model):
    """Model for the 'PhiConstants' database table.'"""

    class Meta:
        db_table = "PhiConstants"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    product = models.IntegerField(db_column="Product", primary_key=True)
    phi = models.FloatField(db_column="phi")
    is_useful = models.BooleanField(db_column="IsUseful", primary_key=True)


class CompletedPhiuTables(models.Model):
    """Model for the 'CompletedPhiuTables' database table.'"""

    class Meta:
        db_table = "CompletedPhiuTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    machine = models.IntegerField(db_column="Machine", primary_key=True)
    eu_product = models.IntegerField(db_column="EuProduct", primary_key=True)
    quantity = models.IntegerField(db_column="Quantity", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    value = models.FloatField(db_column="Value")
    phi_source = models.IntegerField(db_column="PhiSource", primary_key=True)


class EtafuPhiuvecs(models.Model):
    """Model for the 'EtafuPhiuvecs' database table.'"""

    class Meta:
        db_table = "EtafuPhiuvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class Etafuvecs(models.Model):
    """Model for the 'Etafuvecs' database table.'"""

    class Meta:
        db_table = "Etafuvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class Phiuvecs(models.Model):
    """Model for the 'Phiuvecs' database table.'"""

    class Meta:
        db_table = "Phiuvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class Phipfvecs(models.Model):
    """Model for the 'Phipfvecs' database table.'"""

    class Meta:
        db_table = "Phipfvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class Phivecs(models.Model):
    """Model for the 'Phivecs' database table.'"""

    class Meta:
        db_table = "Phivecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTFinalIEA(models.Model):
    """Model for the 'PSUTFinalIEA' database table.'"""

    class Meta:
        db_table = "PSUTFinalIEA"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTUsefulIEAWithDetails(models.Model):
    """Model for the 'PSUTUsefulIEAWithDetails' database table.'"""

    class Meta:
        db_table = "PSUTUsefulIEAWithDetails"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTUsefulIEA(models.Model):
    """Model for the 'PSUTUsefulIEA' database table.'"""

    class Meta:
        db_table = "PSUTUsefulIEA"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class YfuUEIOUfudetailsEnergy(models.Model):
    """Model for the 'YfuUEIOUfudetailsEnergy' database table.'"""

    class Meta:
        db_table = "YfuUEIOUfudetailsEnergy"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class YfuUEIOUfudetailsExergy(models.Model):
    """Model for the 'YfuUEIOUfudetailsExergy' database table.'"""

    class Meta:
        db_table = "YfuUEIOUfudetailsExergy"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class YfuUEIOUfudetails(models.Model):
    """Model for the 'YfuUEIOUfudetails' database table.'"""

    class Meta:
        db_table = "YfuUEIOUfudetails"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTIEA(models.Model):
    """Model for the 'PSUTIEA' database table.'"""

    class Meta:
        db_table = "PSUTIEA"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTMWEnergy(models.Model):
    """Model for the 'PSUTMWEnergy' database table.'"""

    class Meta:
        db_table = "PSUTMWEnergy"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PhivecsMW(models.Model):
    """Model for the 'PhivecsMW' database table.'"""

    class Meta:
        db_table = "PhivecsMW"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTMWAllYears(models.Model):
    """Model for the 'PSUTMWAllYears' database table.'"""

    class Meta:
        db_table = "PSUTMWAllYears"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTMW(models.Model):
    """Model for the 'PSUTMW' database table.'"""

    class Meta:
        db_table = "PSUTMW"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTIEAMW(models.Model):
    """Model for the 'PSUTIEAMW' database table.'"""

    class Meta:
        db_table = "PSUTIEAMW"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTWithNEU(models.Model):
    """Model for the 'PSUTWithNEU' database table.'"""

    class Meta:
        db_table = "PSUTWithNEU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTWithoutNEU(models.Model):
    """Model for the 'PSUTWithoutNEU' database table.'"""

    class Meta:
        db_table = "PSUTWithoutNEU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUT(models.Model):
    """Model for the 'PSUT' database table.'"""

    class Meta:
        db_table = "PSUT"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    includes_neu = models.IntegerField(db_column="IncludesNEU", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class CmatsAgg(models.Model):
    """Model for the 'CmatsAgg' database table.'"""

    class Meta:
        db_table = "CmatsAgg"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class EtafuYEIOU(models.Model):
    """Model for the 'EtafuYEIOU' database table.'"""

    class Meta:
        db_table = "EtafuYEIOU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class EtafuYEIOUagg(models.Model):
    """Model for the 'EtafuYEIOUagg' database table.'"""

    class Meta:
        db_table = "EtafuYEIOUagg"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class Etai(models.Model):
    """Model for the 'Etai' database table.'"""

    class Meta:
        db_table = "Etai"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    includes_neu = models.IntegerField(db_column="IncludesNEU", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTReAll(models.Model):
    """Model for the 'PSUTReAll' database table.'"""

    class Meta:
        db_table = "PSUTReAll"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    includes_neu = models.IntegerField(db_column="IncludesNEU", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class PSUTReAllChopAllDsAllGrAll(models.Model):
    """Model for the 'PSUTReAllChopAllDsAllGrAll' database table.'"""

    class Meta:
        db_table = "PSUTReAllChopAllDsAllGrAll"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    includes_neu = models.IntegerField(db_column="IncludesNEU", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    chopped_mat = models.IntegerField(db_column="ChoppedMat", primary_key=True)
    chopped_var = models.IntegerField(db_column="ChoppedVar", primary_key=True)
    product_aggregation = models.IntegerField(
        db_column="ProductAggregation", primary_key=True
    )
    industry_aggregation = models.IntegerField(
        db_column="IndustryAggregation", primary_key=True
    )
    matname = models.IntegerField(db_column="matname", primary_key=True)
    i = models.IntegerField(db_column="i", primary_key=True)
    j = models.IntegerField(db_column="j", primary_key=True)
    value = models.FloatField(db_column="value")


class SectorAggEtaFU(models.Model):
    """Model for the 'SectorAggEtaFU' database table.'"""

    class Meta:
        db_table = "SectorAggEtaFU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    includes_neu = models.IntegerField(db_column="IncludesNEU", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    chopped_mat = models.IntegerField(db_column="ChoppedMat", primary_key=True)
    chopped_var = models.IntegerField(db_column="ChoppedVar", primary_key=True)
    product_aggregation = models.IntegerField(
        db_column="ProductAggregation", primary_key=True
    )
    industry_aggregation = models.IntegerField(
        db_column="IndustryAggregation", primary_key=True
    )
    gross_net = models.IntegerField(db_column="GrossNet", primary_key=True)
    sector = models.IntegerField(db_column="Sector", primary_key=True)
    final = models.FloatField(db_column="Final")
    useful = models.FloatField(db_column="Useful")
    etafu = models.FloatField(db_column="etafu")


class AggEtaPFU(models.Model):
    """Model for the 'AggEtaPFU' database table.'"""

    class Meta:
        db_table = "AggEtaPFU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset", primary_key=True)
    valid_from_version = models.IntegerField(
        db_column="ValidFromVersion", primary_key=True
    )
    valid_to_version = models.IntegerField(db_column="ValidToVersion", primary_key=True)
    country = models.IntegerField(db_column="Country", primary_key=True)
    method = models.IntegerField(db_column="Method", primary_key=True)
    energy_type = models.IntegerField(db_column="EnergyType", primary_key=True)
    last_stage = models.IntegerField(db_column="LastStage", primary_key=True)
    includes_neu = models.IntegerField(db_column="IncludesNEU", primary_key=True)
    year = models.IntegerField(db_column="Year", primary_key=True)
    chopped_mat = models.IntegerField(db_column="ChoppedMat", primary_key=True)
    chopped_var = models.IntegerField(db_column="ChoppedVar", primary_key=True)
    product_aggregation = models.IntegerField(
        db_column="ProductAggregation", primary_key=True
    )
    industry_aggregation = models.IntegerField(
        db_column="IndustryAggregation", primary_key=True
    )
    gross_net = models.IntegerField(db_column="GrossNet", primary_key=True)
    ex_p = models.FloatField(db_column="EXp")
    ex_f = models.FloatField(db_column="EXf")
    ex_u = models.FloatField(db_column="EXu")
    etapf = models.FloatField(db_column="etapf")
    etafu = models.FloatField(db_column="etafu")
    etapu = models.FloatField(db_column="etapu")
