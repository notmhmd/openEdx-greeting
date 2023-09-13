from rest_framework.serializers import ModelSerializer
from .models import Greeting


class GreetingSerializer(ModelSerializer):
    class Meta:
        model = Greeting
        fields = "__all__"
