from rest_framework import serializers

# model we want to serialize, in our models.py file
from .models import RideData #, MotionData, OceanData

# serializeres are responsible for translating json into model querysets and 
# saving the generated queryset to our database
class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideData
        # we want to serialize all fields
        fields = '__all__'


# class OceanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OceanData
#         fields = '__all__'


# class MotionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MotionData
#         fields = '__all__'