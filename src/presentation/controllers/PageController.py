from django.http import JsonResponse
from application.services import PagesService

def pages(request):
    pages = PagesService.getAllPages()
    data = {
        'error': False,
        'pages': pages
    }
    return JsonResponse(data)