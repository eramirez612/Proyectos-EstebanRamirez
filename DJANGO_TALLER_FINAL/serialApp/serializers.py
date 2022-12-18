from rest_framework import serializers
from serialApp.models import Inscritos, Instituciones

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'

class InstitucionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = '__all__'
    