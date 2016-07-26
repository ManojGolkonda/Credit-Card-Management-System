from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.r

class Card(models.Model):
    friendly_name = models.CharField(max_length=32)
    name_on_card = models.CharField(max_length=32)
    expiry_date = models.DateField()
    card_number = models.CharField(max_length=16)
    type = models.CharField(max_length=32)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.friendly_name