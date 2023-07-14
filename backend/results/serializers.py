from rest_framework.serializers import ModelSerializer
from .models import Result, ResultDetailModel
class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ("name", "description", "drink_count",)

class ResultDetailSerializer(ModelSerializer):
    class Meta:
        model = ResultDetailModel
        fields = ("drink_name", "description", "before_result",)