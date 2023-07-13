from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ResultSerializer
from .models import Result
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
    
# Create your views here.
