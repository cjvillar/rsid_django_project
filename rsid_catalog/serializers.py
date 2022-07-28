from rest_framework import serializers 
from .models import Rsids

class RsidsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rsids
        fields = ['rs_id','gene','diseases']