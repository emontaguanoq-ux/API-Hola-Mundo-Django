from django.http import JsonResponse

def hola_mundo(request):
    return JsonResponse({
        "mensaje": "Hola Mundo",
        "lenguaje": "Python",
        "framework": "Django"
    })
# Create your views here.
