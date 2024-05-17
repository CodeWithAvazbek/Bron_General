from django.db import models
import uuid


class CarCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    name = models.CharField(max_length=120)
    ordering_num = models.IntegerField()
    parent = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class CarColor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    name = models.CharField(max_length=100)
    hex_format = models.IntegerField()

    def __str__(self):
        return self.name
