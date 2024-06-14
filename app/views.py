from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from app.models import Infraccion, Vehiculo, Persona
from app.serializers import (CrearInfraccionSerializer,
                             GenerarInformeSerializer,
                             PersonaSerializer,
                             VehiculoSerializer,
                             InfraccionSerializer)


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self):
        content = {'message': 'only auth user should see'}
        return Response(content)


def vehiculo_exists(patente):
    return Vehiculo.objects.filter(patente=patente).exists()


class CargarInfraccion(APIView):
    serializer_class = CrearInfraccionSerializer

    @extend_schema(request=CrearInfraccionSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        try:
            if not serializer.is_valid():
                return Response("{'message': 'Iternal server error'}", status=status.HTTP_400_BAD_REQUEST)

            patente = serializer.validated_data['patente']
            timestamp = serializer.validated_data['timestamp']
            comentarios = serializer.validated_data['comentarios']
            if not vehiculo_exists(patente):
                return Response("{'message': 'Patente inexistente'}", status=status.HTTP_404_NOT_FOUND)

            infraccion = Infraccion(patente=patente, timestamp=timestamp, comentarios=comentarios)
            infraccion.save()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response("{'message': 'Internal server error'}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenerarInforme(APIView):
    serializer_class = GenerarInformeSerializer
    authentication_classes = []
    permission_classes = []

    @extend_schema(request=GenerarInformeSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        persona = get_object_or_404(Persona, correoElectronico=email)

        try:
            persona_serializer = PersonaSerializer(persona)
            persona_data = persona_serializer.data
            persona_data['vehiculos'] = []

            vehiculos = persona.vehiculos.all()
            # obtener id de la persona
            # Infraccion.objects.filter(patente__propietario="id de la persona" )

            for vehiculo in vehiculos:
                vehiculo_serializer = VehiculoSerializer(vehiculo)
                vehiculo_data = vehiculo_serializer.data
                vehiculo_data['infracciones'] = []

                infracciones = Infraccion.objects.filter(patente=vehiculo.patente)

                for infraccion in infracciones:
                    infraccion_serializer = InfraccionSerializer(infraccion)
                    infraccion_data = infraccion_serializer.data
                    vehiculo_data['infracciones'].append(infraccion_data)

                persona_data['vehiculos'].append(vehiculo_data)

            return Response(persona_data, status=status.HTTP_200_OK)
        except Exception:
            return Response("{'message': 'Persona not found'}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

