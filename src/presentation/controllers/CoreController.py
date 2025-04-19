from django.http import JsonResponse


def health(request):
    data = {"error": False}
    return JsonResponse(data)
