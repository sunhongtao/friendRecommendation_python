# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class MbContent(models.Model):
    userid = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mb_content'


class NineMonthkeys(models.Model):
    uid = models.CharField(max_length=255)
    posttime = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nine_monthkeys'


class Recommendlist(models.Model):
    id = models.IntegerField(primary_key=True)
    suid = models.IntegerField(blank=True, null=True)
    tuid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommendlist'


class Similaritydict(models.Model):
    field_id = models.CharField(db_column='\ufeffid', primary_key=True, max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    wordid = models.CharField(max_length=255, blank=True, null=True)
    word = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'similaritydict'


class Tuidoffollows(models.Model):
    number_1043325954 = models.CharField(db_column='1043325954', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1035997554 = models.CharField(db_column='1035997554', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tuidoffollows'


class UserFeature(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    posttime = models.CharField(max_length=255, blank=True, null=True)
    key1 = models.CharField(max_length=255, blank=True, null=True)
    key2 = models.CharField(max_length=255, blank=True, null=True)
    key3 = models.CharField(max_length=255, blank=True, null=True)
    key4 = models.CharField(max_length=255, blank=True, null=True)
    key5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user-feature'


class Userweibo(models.Model):
    uid = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userweibo'


class WeiboContent(models.Model):
    userid = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weibo-content'
