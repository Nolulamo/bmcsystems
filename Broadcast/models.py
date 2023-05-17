from django.db import models

# Create your models here.
class Broad(models.Model):
    availabilty_of_signal = models.BooleanField(default=False)
    voltage = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-date_created',)

