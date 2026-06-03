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
    """Model for the 'Papers' database table."""

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
    """Model for the 'Dataset' database table."""

    class Meta:
        db_table = "Dataset"
        managed = False

    dataset_id = models.IntegerField(db_column="DatasetID", primary_key=True)
    dataset = models.TextField(db_column="Dataset")
    public = models.BooleanField(db_column="Public")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class Version(models.Model):
    """Model for the 'Version' database table."""

    class Meta:
        db_table = "Version"
        managed = False

    version_id = models.IntegerField(db_column="VersionID", primary_key=True)
    version = models.TextField(db_column="Version")
    release_date = models.TextField(db_column="ReleaseDate")
    public = models.BooleanField(db_column="Public")
    change_notes = models.TextField(db_column="ChangeNotes")


class Country(models.Model):
    """Model for the 'Country' database table."""

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
    """Model for the 'Year' database table."""

    class Meta:
        db_table = "Year"
        managed = False

    year_id = models.IntegerField(db_column="YearID", primary_key=True)
    year = models.IntegerField(db_column="Year")


class Method(models.Model):
    """Model for the 'Method' database table."""

    class Meta:
        db_table = "Method"
        managed = False

    method_id = models.IntegerField(db_column="MethodID", primary_key=True)
    method = models.TextField(db_column="Method")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class EnergyType(models.Model):
    """Model for the 'EnergyType' database table."""

    class Meta:
        db_table = "EnergyType"
        managed = False

    energy_type_id = models.IntegerField(db_column="EnergyTypeID", primary_key=True)
    energy_type = models.TextField(db_column="EnergyType")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class ECCStage(models.Model):
    """Model for the 'ECCStage' database table."""

    class Meta:
        db_table = "ECCStage"
        managed = False

    ecc_stage_id = models.IntegerField(db_column="ECCStageID", primary_key=True)
    ecc_stage = models.TextField(db_column="ECCStage")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class IEALedgerSide(models.Model):
    """Model for the 'IEALedgerSide' database table."""

    class Meta:
        db_table = "IEALedgerSide"
        managed = False

    iea_ledger_side_id = models.IntegerField(
        db_column="IEALedgerSideID", primary_key=True
    )
    iea_ledger_side = models.TextField(db_column="IEALedgerSide")


class IEAFlowAggregationPoint(models.Model):
    """Model for the 'IEAFlowAggregationPoint' database table."""

    class Meta:
        db_table = "IEAFlowAggregationPoint"
        managed = False

    iea_flow_aggregation_point_id = models.IntegerField(
        db_column="IEAFlowAggregationPointID", primary_key=True
    )
    iea_flow_aggregation_point = models.TextField(db_column="IEAFlowAggregationPoint")


class Index(models.Model):
    """Model for the 'Index' database table."""

    class Meta:
        db_table = "Index"
        managed = False

    index_id = models.IntegerField(db_column="IndexID", primary_key=True)
    index = models.TextField(db_column="Index")
    order = models.IntegerField(db_column="Order")
    sankey_column = models.IntegerField(db_column="SankeyColumn")


class Unit(models.Model):
    """Model for the 'Unit' database table."""

    class Meta:
        db_table = "Unit"
        managed = False

    unit_id = models.IntegerField(db_column="UnitID", primary_key=True)
    unit = models.TextField(db_column="Unit")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class AggLevel(models.Model):
    """Model for the 'AggLevel' database table."""

    class Meta:
        db_table = "AggLevel"
        managed = False

    agg_level_id = models.IntegerField(db_column="AggLevelID", primary_key=True)
    agg_level = models.TextField(db_column="AggLevel")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class GrossNet(models.Model):
    """Model for the 'GrossNet' database table."""

    class Meta:
        db_table = "GrossNet"
        managed = False

    gross_net_id = models.IntegerField(db_column="GrossNetID", primary_key=True)
    gross_net = models.TextField(db_column="GrossNet")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class Matname(models.Model):
    """Model for the 'matname' database table."""

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
    """Model for the 'IndProdType' database table."""

    class Meta:
        db_table = "IndProdType"
        managed = False

    ind_prod_type_id = models.IntegerField(db_column="IndProdTypeID", primary_key=True)
    ind_prod_type = models.TextField(db_column="IndProdType")


class RCType(models.Model):
    """Model for the 'RCType' database table."""

    class Meta:
        db_table = "RCType"
        managed = False

    rc_type_id = models.IntegerField(db_column="RCTypeID", primary_key=True)
    rc_type = models.TextField(db_column="RCType")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class IncludesNEU(models.Model):
    """Model for the 'IncludesNEU' database table."""

    class Meta:
        db_table = "IncludesNEU"
        managed = False

    includes_neuid = models.IntegerField(db_column="IncludesNEUID", primary_key=True)
    includes_neu = models.BooleanField(db_column="IncludesNEU")
    full_name = models.TextField(db_column="FullName")
    description = models.TextField(db_column="Description")


class Quantity(models.Model):
    """Model for the 'Quantity' database table."""

    class Meta:
        db_table = "Quantity"
        managed = False

    quantity_id = models.IntegerField(db_column="QuantityID", primary_key=True)
    quantity = models.TextField(db_column="Quantity")


class Species(models.Model):
    """Model for the 'Species' database table."""

    class Meta:
        db_table = "Species"
        managed = False

    species_id = models.IntegerField(db_column="SpeciesID", primary_key=True)
    species = models.TextField(db_column="Species")


class PhiSource(models.Model):
    """Model for the 'PhiSource' database table."""

    class Meta:
        db_table = "PhiSource"
        managed = False

    phi_source_id = models.IntegerField(db_column="PhiSourceID", primary_key=True)
    phi_source = models.TextField(db_column="PhiSource")


class MatnameRCType(models.Model):
    """Model for the 'matnameRCType' database table."""

    class Meta:
        db_table = "matnameRCType"
        managed = False

    matname = models.IntegerField(db_column="matname", primary_key=True)
    rowtype = models.IntegerField(db_column="rowtype")
    coltype = models.IntegerField(db_column="coltype")


class AllIEAData(models.Model):
    """Model for the 'AllIEAData' database table."""

    class Meta:
        db_table = "AllIEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    ledger_side = models.IntegerField(db_column="LedgerSide")
    flow_aggregation_point = models.IntegerField(db_column="FlowAggregationPoint")
    flow = models.IntegerField(db_column="Flow")
    product = models.IntegerField(db_column="Product")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "ledger_side",
        "flow_aggregation_point",
        "flow",
        "product",
    )


class IEAData(models.Model):
    """Model for the 'IEAData' database table."""

    class Meta:
        db_table = "IEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    ledger_side = models.IntegerField(db_column="LedgerSide")
    flow_aggregation_point = models.IntegerField(db_column="FlowAggregationPoint")
    flow = models.IntegerField(db_column="Flow")
    product = models.IntegerField(db_column="Product")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "ledger_side",
        "flow_aggregation_point",
        "flow",
        "product",
    )


class BalancedIEAData(models.Model):
    """Model for the 'BalancedIEAData' database table."""

    class Meta:
        db_table = "BalancedIEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    ledger_side = models.IntegerField(db_column="LedgerSide")
    flow_aggregation_point = models.IntegerField(db_column="FlowAggregationPoint")
    flow = models.IntegerField(db_column="Flow")
    product = models.IntegerField(db_column="Product")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "ledger_side",
        "flow_aggregation_point",
        "flow",
        "product",
    )


class SpecifiedIEAData(models.Model):
    """Model for the 'SpecifiedIEAData' database table."""

    class Meta:
        db_table = "SpecifiedIEAData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    ledger_side = models.IntegerField(db_column="LedgerSide")
    flow_aggregation_point = models.IntegerField(db_column="FlowAggregationPoint")
    flow = models.IntegerField(db_column="Flow")
    product = models.IntegerField(db_column="Product")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "ledger_side",
        "flow_aggregation_point",
        "flow",
        "product",
    )


class AMWPFUDataRaw(models.Model):
    """Model for the 'AMWPFUDataRaw' database table."""

    class Meta:
        db_table = "AMWPFUDataRaw"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    year = models.IntegerField(db_column="Year")
    species = models.IntegerField(db_column="Species")
    stage = models.IntegerField(db_column="Stage")
    sector = models.IntegerField(db_column="Sector")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "year",
        "species",
        "stage",
        "sector",
        "unit",
    )


class AMWPFUData(models.Model):
    """Model for the 'AMWPFUData' database table."""

    class Meta:
        db_table = "AMWPFUData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    year = models.IntegerField(db_column="Year")
    species = models.IntegerField(db_column="Species")
    stage = models.IntegerField(db_column="Stage")
    sector = models.IntegerField(db_column="Sector")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "year",
        "species",
        "stage",
        "sector",
        "unit",
    )


class HMWPFUDataRaw(models.Model):
    """Model for the 'HMWPFUDataRaw' database table."""

    class Meta:
        db_table = "HMWPFUDataRaw"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    year = models.IntegerField(db_column="Year")
    species = models.IntegerField(db_column="Species")
    stage = models.IntegerField(db_column="Stage")
    sector = models.IntegerField(db_column="Sector")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "year",
        "species",
        "stage",
        "sector",
        "unit",
    )


class HMWPFUData(models.Model):
    """Model for the 'HMWPFUData' database table."""

    class Meta:
        db_table = "HMWPFUData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    year = models.IntegerField(db_column="Year")
    species = models.IntegerField(db_column="Species")
    stage = models.IntegerField(db_column="Stage")
    sector = models.IntegerField(db_column="Sector")
    unit = models.IntegerField(db_column="Unit")
    edot = models.FloatField(db_column="Edot")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "year",
        "species",
        "stage",
        "sector",
        "unit",
    )


class IncompleteAllocationTables(models.Model):
    """Model for the 'IncompleteAllocationTables' database table."""

    class Meta:
        db_table = "IncompleteAllocationTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    ledger_side = models.IntegerField(db_column="LedgerSide")
    flow_aggregation_point = models.IntegerField(db_column="FlowAggregationPoint")
    ef_product = models.IntegerField(db_column="EfProduct")
    machine = models.IntegerField(db_column="Machine")
    eu_product = models.IntegerField(db_column="EuProduct")
    destination = models.IntegerField(db_column="Destination")
    quantity = models.IntegerField(db_column="Quantity")
    year = models.IntegerField(db_column="Year")
    value = models.FloatField(db_column="Value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "ledger_side",
        "flow_aggregation_point",
        "ef_product",
        "machine",
        "eu_product",
        "destination",
        "quantity",
        "year",
    )


class CompletedAllocationTables(models.Model):
    """Model for the 'CompletedAllocationTables' database table."""

    class Meta:
        db_table = "CompletedAllocationTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    ledger_side = models.IntegerField(db_column="LedgerSide")
    flow_aggregation_point = models.IntegerField(db_column="FlowAggregationPoint")
    ef_product = models.IntegerField(db_column="EfProduct")
    machine = models.IntegerField(db_column="Machine")
    eu_product = models.IntegerField(db_column="EuProduct")
    destination = models.IntegerField(db_column="Destination")
    quantity = models.IntegerField(db_column="Quantity")
    year = models.IntegerField(db_column="Year")
    value = models.FloatField(db_column="Value")
    c_source = models.IntegerField(db_column="CSource")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "ledger_side",
        "flow_aggregation_point",
        "ef_product",
        "machine",
        "eu_product",
        "destination",
        "quantity",
        "year",
        "c_source",
    )


class Cmats(models.Model):
    """Model for the 'Cmats' database table."""

    class Meta:
        db_table = "Cmats"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class AllMachineData(models.Model):
    """Model for the 'AllMachineData' database table."""

    class Meta:
        db_table = "AllMachineData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    machine = models.IntegerField(db_column="Machine")
    eu_product = models.IntegerField(db_column="EuProduct")
    quantity = models.IntegerField(db_column="Quantity")
    year = models.IntegerField(db_column="Year")
    value = models.FloatField(db_column="Value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "machine",
        "eu_product",
        "quantity",
        "year",
    )


class MachineData(models.Model):
    """Model for the 'MachineData' database table."""

    class Meta:
        db_table = "MachineData"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    machine = models.IntegerField(db_column="Machine")
    eu_product = models.IntegerField(db_column="EuProduct")
    quantity = models.IntegerField(db_column="Quantity")
    year = models.IntegerField(db_column="Year")
    value = models.FloatField(db_column="Value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "machine",
        "eu_product",
        "quantity",
        "year",
    )


class CompletedEfficiencyTables(models.Model):
    """Model for the 'CompletedEfficiencyTables' database table."""

    class Meta:
        db_table = "CompletedEfficiencyTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    machine = models.IntegerField(db_column="Machine")
    eu_product = models.IntegerField(db_column="EuProduct")
    quantity = models.IntegerField(db_column="Quantity")
    year = models.IntegerField(db_column="Year")
    value = models.FloatField(db_column="Value")
    etafu_source = models.IntegerField(db_column="etafuSource")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "machine",
        "eu_product",
        "quantity",
        "year",
        "etafu_source",
    )


class PhiConstants(models.Model):
    """Model for the 'PhiConstants' database table."""

    class Meta:
        db_table = "PhiConstants"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    product = models.IntegerField(db_column="Product")
    phi = models.FloatField(db_column="phi")
    is_useful = models.BooleanField(db_column="IsUseful")

    pk = models.CompositePrimaryKey(
        "dataset", "valid_from_version", "valid_to_version", "product", "is_useful"
    )


class CompletedPhiuTables(models.Model):
    """Model for the 'CompletedPhiuTables' database table."""

    class Meta:
        db_table = "CompletedPhiuTables"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    machine = models.IntegerField(db_column="Machine")
    eu_product = models.IntegerField(db_column="EuProduct")
    quantity = models.IntegerField(db_column="Quantity")
    year = models.IntegerField(db_column="Year")
    value = models.FloatField(db_column="Value")
    phi_source = models.IntegerField(db_column="PhiSource")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "machine",
        "eu_product",
        "quantity",
        "year",
        "phi_source",
    )


class EtafuPhiuvecs(models.Model):
    """Model for the 'EtafuPhiuvecs' database table."""

    class Meta:
        db_table = "EtafuPhiuvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "year",
        "matname",
        "i",
        "j",
    )


class Etafuvecs(models.Model):
    """Model for the 'Etafuvecs' database table."""

    class Meta:
        db_table = "Etafuvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "year",
        "matname",
        "i",
        "j",
    )


class Phiuvecs(models.Model):
    """Model for the 'Phiuvecs' database table."""

    class Meta:
        db_table = "Phiuvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "year",
        "matname",
        "i",
        "j",
    )


class Phipfvecs(models.Model):
    """Model for the 'Phipfvecs' database table."""

    class Meta:
        db_table = "Phipfvecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    method = models.IntegerField(db_column="Method")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "energy_type",
        "last_stage",
        "method",
        "year",
        "matname",
        "i",
        "j",
    )


class Phivecs(models.Model):
    """Model for the 'Phivecs' database table."""

    class Meta:
        db_table = "Phivecs"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTFinalIEA(models.Model):
    """Model for the 'PSUTFinalIEA' database table."""

    class Meta:
        db_table = "PSUTFinalIEA"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTUsefulIEAWithDetails(models.Model):
    """Model for the 'PSUTUsefulIEAWithDetails' database table."""

    class Meta:
        db_table = "PSUTUsefulIEAWithDetails"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTUsefulIEA(models.Model):
    """Model for the 'PSUTUsefulIEA' database table."""

    class Meta:
        db_table = "PSUTUsefulIEA"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class YfuUEIOUfudetailsEnergy(models.Model):
    """Model for the 'YfuUEIOUfudetailsEnergy' database table."""

    class Meta:
        db_table = "YfuUEIOUfudetailsEnergy"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class YfuUEIOUfudetailsExergy(models.Model):
    """Model for the 'YfuUEIOUfudetailsExergy' database table."""

    class Meta:
        db_table = "YfuUEIOUfudetailsExergy"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class YfuUEIOUfudetails(models.Model):
    """Model for the 'YfuUEIOUfudetails' database table."""

    class Meta:
        db_table = "YfuUEIOUfudetails"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTIEA(models.Model):
    """Model for the 'PSUTIEA' database table."""

    class Meta:
        db_table = "PSUTIEA"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTMWEnergy(models.Model):
    """Model for the 'PSUTMWEnergy' database table."""

    class Meta:
        db_table = "PSUTMWEnergy"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PhivecsMW(models.Model):
    """Model for the 'PhivecsMW' database table."""

    class Meta:
        db_table = "PhivecsMW"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTMWAllYears(models.Model):
    """Model for the 'PSUTMWAllYears' database table."""

    class Meta:
        db_table = "PSUTMWAllYears"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTMW(models.Model):
    """Model for the 'PSUTMW' database table."""

    class Meta:
        db_table = "PSUTMW"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTIEAMW(models.Model):
    """Model for the 'PSUTIEAMW' database table."""

    class Meta:
        db_table = "PSUTIEAMW"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTWithNEU(models.Model):
    """Model for the 'PSUTWithNEU' database table."""

    class Meta:
        db_table = "PSUTWithNEU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTWithoutNEU(models.Model):
    """Model for the 'PSUTWithoutNEU' database table."""

    class Meta:
        db_table = "PSUTWithoutNEU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUT(models.Model):
    """Model for the 'PSUT' database table."""

    class Meta:
        db_table = "PSUT"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    includes_neu = models.IntegerField(db_column="IncludesNEU")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "includes_neu",
        "year",
        "matname",
        "i",
        "j",
    )


class CmatsAgg(models.Model):
    """Model for the 'CmatsAgg' database table."""

    class Meta:
        db_table = "CmatsAgg"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class EtafuYEIOU(models.Model):
    """Model for the 'EtafuYEIOU' database table."""

    class Meta:
        db_table = "EtafuYEIOU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "year",
        "matname",
        "i",
        "j",
    )


class EtafuYEIOUagg(models.Model):
    """Model for the 'EtafuYEIOUagg' database table."""

    class Meta:
        db_table = "EtafuYEIOUagg"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "year",
        "matname",
        "i",
        "j",
    )


class Etai(models.Model):
    """Model for the 'Etai' database table."""

    class Meta:
        db_table = "Etai"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    includes_neu = models.IntegerField(db_column="IncludesNEU")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "includes_neu",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTReAll(models.Model):
    """Model for the 'PSUTReAll' database table."""

    class Meta:
        db_table = "PSUTReAll"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    includes_neu = models.IntegerField(db_column="IncludesNEU")
    year = models.IntegerField(db_column="Year")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "includes_neu",
        "year",
        "matname",
        "i",
        "j",
    )


class PSUTReAllChopAllDsAllGrAll(models.Model):
    """Model for the 'PSUTReAllChopAllDsAllGrAll' database table."""

    class Meta:
        db_table = "PSUTReAllChopAllDsAllGrAll"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    includes_neu = models.IntegerField(db_column="IncludesNEU")
    year = models.IntegerField(db_column="Year")
    chopped_mat = models.IntegerField(db_column="ChoppedMat")
    chopped_var = models.IntegerField(db_column="ChoppedVar")
    product_aggregation = models.IntegerField(db_column="ProductAggregation")
    industry_aggregation = models.IntegerField(db_column="IndustryAggregation")
    matname = models.IntegerField(db_column="matname")
    i = models.IntegerField(db_column="i")
    j = models.IntegerField(db_column="j")
    value = models.FloatField(db_column="value")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "includes_neu",
        "year",
        "chopped_mat",
        "chopped_var",
        "product_aggregation",
        "industry_aggregation",
        "matname",
        "i",
        "j",
    )


class SectorAggEtaFU(models.Model):
    """Model for the 'SectorAggEtaFU' database table."""

    class Meta:
        db_table = "SectorAggEtaFU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    includes_neu = models.IntegerField(db_column="IncludesNEU")
    year = models.IntegerField(db_column="Year")
    chopped_mat = models.IntegerField(db_column="ChoppedMat")
    chopped_var = models.IntegerField(db_column="ChoppedVar")
    product_aggregation = models.IntegerField(db_column="ProductAggregation")
    industry_aggregation = models.IntegerField(db_column="IndustryAggregation")
    gross_net = models.IntegerField(db_column="GrossNet")
    sector = models.IntegerField(db_column="Sector")
    final = models.FloatField(db_column="Final")
    useful = models.FloatField(db_column="Useful")
    etafu = models.FloatField(db_column="etafu")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "includes_neu",
        "year",
        "chopped_mat",
        "chopped_var",
        "product_aggregation",
        "industry_aggregation",
        "gross_net",
        "sector",
    )


class AggEtaPFU(models.Model):
    """Model for the 'AggEtaPFU' database table."""

    class Meta:
        db_table = "AggEtaPFU"
        managed = False

    dataset = models.IntegerField(db_column="Dataset")
    valid_from_version = models.IntegerField(db_column="ValidFromVersion")
    valid_to_version = models.IntegerField(db_column="ValidToVersion")
    country = models.IntegerField(db_column="Country")
    method = models.IntegerField(db_column="Method")
    energy_type = models.IntegerField(db_column="EnergyType")
    last_stage = models.IntegerField(db_column="LastStage")
    includes_neu = models.IntegerField(db_column="IncludesNEU")
    year = models.IntegerField(db_column="Year")
    chopped_mat = models.IntegerField(db_column="ChoppedMat")
    chopped_var = models.IntegerField(db_column="ChoppedVar")
    product_aggregation = models.IntegerField(db_column="ProductAggregation")
    industry_aggregation = models.IntegerField(db_column="IndustryAggregation")
    gross_net = models.IntegerField(db_column="GrossNet")
    ex_p = models.FloatField(db_column="EXp")
    ex_f = models.FloatField(db_column="EXf")
    ex_u = models.FloatField(db_column="EXu")
    etapf = models.FloatField(db_column="etapf")
    etafu = models.FloatField(db_column="etafu")
    etapu = models.FloatField(db_column="etapu")

    pk = models.CompositePrimaryKey(
        "dataset",
        "valid_from_version",
        "valid_to_version",
        "country",
        "method",
        "energy_type",
        "last_stage",
        "includes_neu",
        "year",
        "chopped_mat",
        "chopped_var",
        "product_aggregation",
        "industry_aggregation",
        "gross_net",
    )
