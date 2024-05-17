from django.db import models
import uuid


class Appeal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    name = models.CharField(max_length=120)
    message = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
