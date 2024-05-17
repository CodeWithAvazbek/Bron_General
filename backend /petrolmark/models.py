from django.db import models
import uuid


class PetrolMark(models.Model):
    class OilType(models.IntegerChoices):
        PETROL = 0, "PETROL"
        DIESEL = 1, "DIESEL"
        GAZ = 2, "GAZ"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    name = models.CharField(max_length=120, unique=True)
    oil_type = models.PositiveSmallIntegerField(choices=OilType.choices, default=OilType.GAZ.value)

    def __str__(self):
        return self.name


# PetrolMark.objects.filter(oil_type=PetrolMark.OilType.PETROL.value)
