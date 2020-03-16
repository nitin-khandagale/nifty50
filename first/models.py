from django.db import models

class Pistol(models.Model):
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    opened = models.FloatField(blank=True, null=True)
    closed = models.FloatField(blank=True, null=True)
    rangee = models.FloatField(blank=True, null=True)
    msf = models.FloatField(db_column='MSF', blank=True, null=True)  # Field name made lowercase.
    jgd = models.FloatField(db_column='JGD', blank=True, null=True)  # Field name made lowercase.
    jwd = models.FloatField(db_column='JWD', blank=True, null=True)  # Field name made lowercase.
    sr = models.AutoField(db_column='Sr', primary_key=True)  # Field name made lowercase.
    directors_pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pistol'
