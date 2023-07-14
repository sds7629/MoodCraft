from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ResultSerializer, ResultDetailSerializer
from .models import Result, ResultDetailModel
class ResultInfo(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Result.objects.get(pk = pk)
    #     except Result.DoesNotExist:
    #         raise NotFound

    def get(self, request, drink_kind):
        # result = self.get_object(pk)
        # result.drink_count += 1
        # result.save()
        # serializer = ResultSerializer(result)
        # return Response(serializer.data)
        result = Result.objects.get(drink_kind = drink_kind)
        result.drink_count += 1
        result.save()
        serializer = ResultSerializer(result)
        return Response(serializer.data)

   
    # def post(self, request, pk):
    #     serializer= ResultSerializer(data = request.data)
    #     if serializer.is_valid():
    #         result= request.data.
    #         serializer = ResultSerializer(result)

class ResultDetail(APIView):
        def get(self, request, drink_kind):
            result = Result.objects.get(drink_kind = drink_kind)
            resultDetail = result.results.all()
            serializer = ResultDetailSerializer(resultDetail, many = True)
            return Response(serializer.data)
# Create your views here.
