# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Phones(models.Model):
    prd_name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phones'


class PhonesHandled(models.Model):
    prd_name = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    sentiments = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phones_handled'
