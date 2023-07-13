from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ResultSerializer, ResultDetailSerializer
from .models import Result, ResultDetailModel
class ResultInfo(APIView):
    def get_object(self, pk):
        try:
            return Result.objects.get(pk = pk)
        except Result.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        result = self.get_object(pk)
        result.drink_count += 1
        result.save()
        serializer = ResultSerializer(result)
        return Response(serializer.data)
    
class ResultDetail(APIView):
    def get(self, request, pk):
        result = ResultDetailModel.objects.all()
        serializer = ResultDetailSerializer(result, many = True)
        return Response(serializer.data)
