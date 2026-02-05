from django.db import models
from production.models import ProductionBatch

class QCParameter(models.Model):
    name = models.CharField(max_length=100)
    min_limit = models.FloatField()
    max_limit = models.FloatField()

    def __str__(self):
        return self.name


class QCTest(models.Model):
    production_batch = models.ForeignKey(ProductionBatch, on_delete=models.CASCADE)
    parameter = models.ForeignKey(QCParameter, on_delete=models.CASCADE)
    value = models.FloatField()
    test_date = models.DateTimeField(auto_now_add=True)

    RESULT = (
        ("PASS", "Pass"),
        ("FAIL", "Fail"),
    )
    result = models.CharField(max_length=10, choices=RESULT)

    def save(self, *args, **kwargs):
        if self.value < self.parameter.min_limit or self.value > self.parameter.max_limit:
            self.result = "FAIL"
            self.production_batch.status = "HOLD"
            self.production_batch.save()
        else:
            self.result = "PASS"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.production_batch.batch_code} - {self.parameter.name}"
