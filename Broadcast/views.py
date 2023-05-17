from django.shortcuts import render
from django.http import HttpResponse
from .models import Broad
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BroadSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):

    return HttpResponse('Hello, world')

def ShowStatus(request):
    show_status = Broad.objects.all()[:1]

    context = {
        'show_status': show_status,
    }

    return render(request, 'broadcast/show.html', context)


@csrf_exempt
@api_view(['POST'])
def PostData(request):
    serializer = BroadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


