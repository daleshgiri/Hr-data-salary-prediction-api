# Create your views here.
from django.http.response import HttpResponse
from rest_framework import viewsets
from hr.models import HR
from hr.myserializer import HRSerializer
from hr import HRDJ
from rest_framework.response import Response

class HRViewSet(viewsets.ModelViewSet):
    queryset = HR.objects.order_by("-id")
    serializer_class = HRSerializer
    def create(self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self, request, *args, **kwargs)
        ob = HR.objects.latest("id")
        left = HRDJ.pred(ob)
        return Response({"status": "Success", "left": left})  # Your override
        
        
