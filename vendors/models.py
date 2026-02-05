from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MaterialBatch(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField()
    received_date = models.DateField(auto_now_add=True)

    QC_STATUS = (
        ("PENDING", "Pending"),
        ("PASS", "Pass"),
        ("FAIL", "Fail"),
    )
    qc_status = models.CharField(max_length=20, choices=QC_STATUS, default="PENDING")

    def __str__(self):
        return f"{self.material.name} - {self.batch_number}"
