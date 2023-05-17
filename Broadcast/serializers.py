from rest_framework import serializers
from .models import Broad

class BroadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broad
        fields = ('availabilty_of_signal', 'voltage')