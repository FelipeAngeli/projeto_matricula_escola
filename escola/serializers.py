from rest_framework import serializers
from escola.models import Estudante, Curso


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'