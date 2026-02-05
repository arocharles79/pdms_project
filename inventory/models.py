from django.db import models
from vendors.models import RawMaterial

class InventoryItem(models.Model):
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    available_stock = models.FloatField(default=0)

    def __str__(self):
        return self.material.name


class StockMovement(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)

    MOVEMENT_TYPE = (
        ("IN", "In"),
        ("OUT", "Out"),
        ("RETURN", "Return"),
        ("DISPATCH", "Dispatch"),
    )
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPE)

    quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.movement_type == "IN" or self.movement_type == "RETURN":
            self.inventory_item.available_stock += self.quantity
        else:
            self.inventory_item.available_stock -= self.quantity

        self.inventory_item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.inventory_item.material.name} - {self.movement_type}"
