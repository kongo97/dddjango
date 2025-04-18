# infrastructure/repositories.py

from core.models import InvoiceModel   # o: from core.models import InvoiceModel
from domain.entities import Invoice

class DjangoInvoiceRepository:
    """
    Repository che mappa gli InvoiceModel di Django
    in entità di dominio Invoice.
    """

    def list_all(self) -> list[Invoice]:
        # prendi tutti i record Django dal DB
        qs = InvoiceModel.objects.all()

        # traduci ciascun record in entità di dominio
        return [
            Invoice(
                id=rec.id,
                customer_name=rec.customer_name,
                amount=rec.amount,
                issued_date=rec.issued_date
            )
            for rec in qs
        ]

    def get_by_id(self, invoice_id: int) -> Invoice | None:
        try:
            rec = InvoiceModel.objects.get(pk=invoice_id)
        except InvoiceModel.DoesNotExist:
            return None
        return Invoice(
            id=rec.id,
            customer_name=rec.customer_name,
            amount=rec.amount,
            issued_date=rec.issued_date
        )

    # qui puoi aggiungere altri metodi: save(), delete(), ecc.
