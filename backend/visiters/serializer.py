from rest_framework.serializers import ModelSerializer
from .models import Visiter,Count


class VisiterSerializer(ModelSerializer):
    class Meta:
        model = Visiter
        fields = "__all__" 

class CountSerializer(ModelSerializer):
    class Meta:
        model = Count
        fields = "__all__"