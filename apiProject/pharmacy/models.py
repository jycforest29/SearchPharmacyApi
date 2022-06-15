# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Convenience(models.Model):
    startdate = models.CharField(db_column='startDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    loadaddress = models.CharField(db_column='loadAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(primary_key = True, blank=True)

    class Meta:
        managed = False
        db_table = 'convenience'


class Hospital(models.Model):
    loadaddress = models.CharField(db_column='loadAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.CharField(db_column='startDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totaldoctor = models.IntegerField(db_column='totalDoctor', blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(primary_key = True, blank=True)

    class Meta:
        managed = False
        db_table = 'hospital'


class Line(models.Model):
    name = models.CharField(primary_key = True, max_length=11, blank=True)

    class Meta:
        managed = False
        db_table = 'line'


class Pharmacy(models.Model):
    loadaddress = models.CharField(db_column='loadAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.CharField(db_column='startDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    index = models.BigIntegerField(primary_key = True, blank=True)

    class Meta:
        managed = False
        db_table = 'pharmacy'


class Pharmacylocation(models.Model):
    loadaddress = models.CharField(db_column='loadAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hospitalcount = models.IntegerField(db_column='hospitalCount', blank=True, null=True)  # Field name made lowercase.
    doctorcount = models.IntegerField(db_column='doctorCount', blank=True, null=True)  # Field name made lowercase.
    pharmacycount = models.IntegerField(db_column='pharmacyCount', blank=True, null=True)  # Field name made lowercase.
    dong = models.CharField(max_length=11, blank=True, null=True)
    conveniencecount = models.IntegerField(db_column='convenienceCount', blank=True, null=True)  # Field name made lowercase.
    hospitalperpharmacy = models.FloatField(db_column='hospitalPerPharmacy', blank=True, null=True)  # Field name made lowercase.
    doctorperpharmacy = models.FloatField(db_column='doctorPerPharmacy', blank=True, null=True)  # Field name made lowercase.
    convenienceperpharmacy = models.FloatField(db_column='conveniencePerPharmacy', blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(primary_key = True, blank=True)
    viewcount = models.IntegerField(db_column='viewCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pharmacylocation'


class Station(models.Model):
    dong = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=11, blank=True, null=True)
    line = models.CharField(max_length=11, blank=True, null=True)
    index = models.IntegerField(primary_key = True, blank=True)

    class Meta:
        managed = False
        db_table = 'station'
