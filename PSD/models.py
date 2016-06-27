from django.db import models
from django.forms import ModelForm

# Create your models here.

#class = table, variable = column
class PSD(models.Model):
    PSD_value = models.FloatField(blank=True, default=0)
    Freq_value = models.FloatField(blank=True, default=0)

    PSD_svg = models.FloatField(blank=True, default=0)
    Freq_svg = models.FloatField(blank=True, default=0)

    sc_tag = models.CharField(blank=True, max_length=200)
