from django.db import models
from vendors.models import MaterialBatch
from django.contrib.auth.models import User

class ProcessStage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductionBatch(models.Model):
    batch_code = models.CharField(max_length=100, unique=True)
    material_batch = models.ForeignKey(MaterialBatch, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)

    STATUS = (
        ("RUNNING", "Running"),
        ("HOLD", "Hold"),
        ("COMPLETED", "Completed"),
    )
    status = models.CharField(max_length=20, choices=STATUS, default="RUNNING")

    def __str__(self):
        return self.batch_code


class StageLog(models.Model):
    production_batch = models.ForeignKey(ProductionBatch, on_delete=models.CASCADE)
    stage = models.ForeignKey(ProcessStage, on_delete=models.CASCADE)
    machine_name = models.CharField(max_length=100)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    input_qty = models.FloatField()
    output_qty = models.FloatField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.production_batch.batch_code} - {self.stage.name}"
