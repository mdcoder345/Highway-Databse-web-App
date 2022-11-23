from django.db import models

class Highway(models.Model):
    highway_number = models.CharField(primary_key=True,max_length=200)
    highway_name = models.CharField(max_length=2000)
    highway_type = models.CharField(max_length=2000)
    total_length_in_km = models.IntegerField()
    number_of_lanes = models.IntegerField()
    built_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'highway'

class Tender(models.Model):
    tender_no = models.BigIntegerField(primary_key=True)
    tender_title = models.CharField(max_length=2000)
    bid_submission_start_date = models.DateField()
    bid_submission_end_date = models.DateField()

    class Meta:
        managed=False
        db_table = 'tenders'
