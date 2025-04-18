from django.shortcuts import render
from application.services import lista_fatture

def invoice_list(request):
    # chiami il service layer
    fatture = lista_fatture()
    return render(request, 'presentation/invoice_list.html', {'fatture': fatture})

def home(request):
    return render(request, 'presentation/home.html')