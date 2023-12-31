from django.db import models

# Create your models here.
class SchoolModel(models.Model):
    name = models.CharField(max_length=65)
    address = models.CharField(max_length=255)
    info = models.JSONField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table='schools'