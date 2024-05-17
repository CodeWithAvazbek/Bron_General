from django.db import models
import uuid


class General(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
