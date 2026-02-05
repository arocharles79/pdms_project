from django.db import models
from production.models import ProductionBatch

class Anomaly(models.Model):
    production_batch = models.ForeignKey(ProductionBatch, on_delete=models.CASCADE)
    description = models.TextField()
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anomaly - {self.production_batch.batch_code}"
