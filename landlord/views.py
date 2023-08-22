from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, tenant. You're on my property."
)
