from django.conf import settings

def api_key(request):
    return {
        'MAPS_API_KEY': settings.MAPS_API_KEY,
    }
