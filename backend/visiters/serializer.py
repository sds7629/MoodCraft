from rest_framework.serializers import ModelSerializer
from .models import Visiter

class VisiterSerializer(ModelSerializer):
    class Meta:
        model = Visiter
<<<<<<< HEAD
        fields = "__all__" 
=======
        fields = "__all__" 

# class CountSerializer(ModelSerializer):
#     class Meta:
#         model = Count
#         fields = "__all__"
>>>>>>> 0f72ee030948cd426dd102df9338d0d358bffc5c
