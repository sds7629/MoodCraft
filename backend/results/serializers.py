from rest_framework.serializers import ModelSerializer
from .models import Result, ResultDetailModel
class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ("name", "description", "drink_count", "image")

class ResultDetailSerializer(ModelSerializer):
    class Meta:
        model = ResultDetailModel
        fields = "__all__"