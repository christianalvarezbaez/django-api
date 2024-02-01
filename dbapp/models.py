# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Clients(models.Model):
    id_client = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class FirstTable(models.Model):
    column1 = models.CharField(max_length=255, blank=True, null=True)
    columna2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'first_table'


class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_schema = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_geography_column = models.TextField(blank=True, null=True)  # This field type is a guess.
    coord_dimension = models.BigIntegerField(blank=True, null=True)
    srid = models.BigIntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geography_columns'
        db_table_comment = "Shows all defined geography columns. Matches PostGIS' geography_columns functionality."


class GeometryColumns(models.Model):
    f_table_catalog = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_schema = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_geometry_column = models.TextField(blank=True, null=True)  # This field type is a guess.
    coord_dimension = models.BigIntegerField(blank=True, null=True)
    srid = models.BigIntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geometry_columns'
        db_table_comment = "Shows all defined geometry columns. Matches PostGIS' geometry_columns functionality."


class KafkaTest(models.Model):
    alpha = models.CharField(max_length=255, blank=True, null=True)
    beta = models.BigIntegerField(blank=True, null=True)
    gamma = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kafka_test'


class SpatialRefSys(models.Model):
    srid = models.BigIntegerField(blank=True, null=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.BigIntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
        db_table_comment = "Shows all defined Spatial Reference Identifiers (SRIDs). Matches PostGIS' spatial_ref_sys table."


class TestingTable(models.Model):
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preguntas = models.TextField(db_column='Preguntas', blank=True, null=True)  # Field name made lowercase.
    correlacion = models.FloatField(db_column='Correlacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testing_table'


class Transactions(models.Model):
    id_client = models.OneToOneField(Clients, models.DO_NOTHING, db_column='id_client', primary_key=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'

################Materialized views####################
        

# Existing models remain unchanged

class TimeSeriesMaterializedView(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    amount_sum = models.FloatField()

    class Meta:
        managed = False
        db_table = 'time_series_materialized_view'

class PieGenderMaterializedView(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=255)
    amount_sum = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pie_gender_materialized_view'

class BoxesGenderMaterializedView(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=255)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'boxes_gender_materialized_view'

class TopClientsMaterializedView(models.Model):
    id = models.IntegerField(primary_key=True)
    id_client = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.FloatField()    

    class Meta:
        managed = False
        db_table = 'topclients_materialized_view'

class AgeRangeMaterializedView(models.Model):
    id = models.IntegerField(primary_key=True)
    age_range = models.CharField(max_length=255)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'agerange_materialized_view'

class AgeHistogramMaterializedView(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'agehistogram_materialized_view'

