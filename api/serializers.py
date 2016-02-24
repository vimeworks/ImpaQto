from rest_framework.serializers import ModelSerializer
from coworkersimpaqto.models import Contrato, Coworker, Consumo, Membresia

class MembresiaSerializer(ModelSerializer):
    class Meta:
        model = Membresia
        fiels = ('nombre','uso_espacio')
        
class CoworkerSerializer(ModelSerializer):
    class Meta:
        model = Coworker
        fields = ('id','nombre','apellido','username','mail')

class ContratoSerializer(ModelSerializer):
    coworker = CoworkerSerializer(many=False,read_only=True)
    membresia = MembresiaSerializer(many=False,read_only=True)
    class Meta:
        model = Contrato
        fields = ('id','fecha_inicio','estado','coworker','tiempo_sobrante','membresia',)

class ConsumoSerializer(ModelSerializer):
    contrato = ContratoSerializer(many=False,read_only=True)
    class Meta:
        model = Consumo
        fields = ('id','contrato','fecha_entrada','fecha_salida','estado_registro','get_estado_registro_display')