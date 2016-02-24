from rest_framework import serializers
from .models import Contrato, Coworker

class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = ('id','fecha_inicio','estado','coworker',)

class CoworkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coworker
        fields = ('nombre','apellido','username',)