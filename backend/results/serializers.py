from rest_framework.serializers import ModelSerializer
from .models import Result, ResultDetailModel
class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

class ResultDetailSerializer(ModelSerializer):
    class Meta:
        model = ResultDetailModel
        fields = ("drink_name", "description",)