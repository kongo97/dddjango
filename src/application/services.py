# application/services.py
from domain.entities import Invoice         # <–– questo ora funziona
from infrastructure.repositories import DjangoInvoiceRepository

def lista_fatture():
    repo = DjangoInvoiceRepository()
    return repo.list_all()
