from django.db import models

# Create your models here.
class NewSpace(models.Model):
    slot_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_created')
    location_details = models.TextField(blank=True,null=True)
    charges = models.IntegerField()

    def __str__(self):
        return self.slot_name

class NewSlot(models.Model):
    slot_list = models.ForeignKey(NewSpace,on_delete=models.CASCADE)
    slot_position = models.CharField(max_length=10)
    slot_status = models.BooleanField(default=False)

    def __str__(self):
        return self.slot_position
