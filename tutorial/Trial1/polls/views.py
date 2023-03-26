
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Yo, Yo I'm the original B.I.G")