from rest_framework import serializers
from .models import Pais, Departamento, Municipio, SectorEmpresarial, TipoUsuario, TipoActividadUsuario, Moneda, CategoriasEmpleos, CategoriaProyectos, Empresa, InstitucionEducativa
from Login.models import Proyecto, PostulacionEmpleo

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class SectorEmpresarialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorEmpresarial
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class TipoActividadUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActividadUsuario
        fields = '__all__'

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'

class CategoriasEmpleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasEmpleos
        fields = '__all__'

class CategoriaProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProyectos
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class InstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitucionEducativa
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class PostulacionEmpleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostulacionEmpleo
        fields = '__all__'