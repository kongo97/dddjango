from django.db import models

class InvoiceModel(models.Model):
    customer_name = models.CharField(max_length=200)
    amount        = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date   = models.DateField()

    def __str__(self):
        return f"Invoice #{self.pk} – {self.customer_name}"
    
    class Meta:
        db_table = 'invoices'
