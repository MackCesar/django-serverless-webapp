from django.db import models
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,editable=False)
    data - models.CharField(max_length=255)

