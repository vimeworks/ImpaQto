#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContratoSerializer, CoworkerSerializer, ConsumoSerializer
from coworkersimpaqto.models import Coworker, Contrato,Consumo
from django.shortcuts import get_object_or_404
from datetime import timezone
import datetime
from _decimal import Decimal


# Create your views here.

class HolaMundo(APIView):
    def get(self, request,username,format=None):
        return Response({'mensaje':'Hola '+username+' mundo de django rest framework'})

hola_mundo = HolaMundo.as_view()

class CoworkerView(APIView):
    serializer_class = CoworkerSerializer
    
    def get(self,request,username=None,format=None):
        if username != None:
            coworkers =get_object_or_404(Coworker,username=username)
            many=False
        else:
            coworkers = Coworker.objects.all()
            many=True
        response = self.serializer_class(coworkers,many=many)
        return Response(response.data)
    
coworker = CoworkerView.as_view()

class ContratoView(APIView):
    serializer_class = ContratoSerializer
    
    def get(self,request,username=None,format=None):
        estado='A'
        if username != None:
            contrato =get_object_or_404(Contrato,estado=estado,coworker__username=username)
            many=False
        else:
            contrato=Contrato.objects.all()
            many=True
        response = self.serializer_class(contrato,many=many)
        return Response(response.data)

contrato = ContratoView.as_view()

class ConsumoRegistroView(APIView):
    serializer_class = ConsumoSerializer
    
    def get(self,request,username=None,format=None):
        
        estado='A'
        estado_registro='E'
        if username !=None:
            contrato =get_object_or_404(Contrato,estado=estado,coworker__username=username)
            id=contrato.id
            try:
                consumo = Consumo.objects.get(estado_registro=estado_registro,contrato__id=id)
                consumo.fecha_salida = datetime.datetime.now(timezone.utc)
                diferencia= consumo.fecha_salida-consumo.fecha_entrada
                consumo.estado_registro = 'S'
                consumo.save()
                sobrante=Decimal(contrato.tiempo_sobrante)
                sobrante_actual=sobrante-Decimal((diferencia.seconds) /60)
                contrato.tiempo_sobrante=sobrante_actual
                contrato.save()
            except Consumo.DoesNotExist:
                consumo = Consumo.objects.create(contrato=contrato)
                consumo.save()  

        
        response = self.serializer_class(consumo,many=False)
        return Response(response.data)
        
        
consumo = ConsumoRegistroView.as_view()