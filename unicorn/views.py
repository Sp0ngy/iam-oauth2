from rest_framework import viewsets

from unicorn.models import Unicorn
from unicorn.serializer import UnicornSerializer


class UnicornViewSet(viewsets.ModelViewSet):
    queryset = Unicorn.objects.all()
    serializer_class = UnicornSerializer
