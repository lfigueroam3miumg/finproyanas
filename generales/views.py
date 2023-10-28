from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Pais, Departamento, Municipio, SectorEmpresarial, TipoUsuario, TipoActividadUsuario, Moneda, CategoriasEmpleos, CategoriaProyectos, Empresa, InstitucionEducativa
from Login.models import Proyecto, PostulacionEmpleo
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer, SectorEmpresarialSerializer, TipoUsuarioSerializer, TipoActividadUsuarioSerializer, MonedaSerializer, CategoriasEmpleosSerializer, CategoriaProyectosSerializer, EmpresaSerializer, InstitucionEducativaSerializer, ProyectoSerializer, PostulacionEmpleoSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        departamentos = Departamento.objects.filter(IdPais=instance)
        departamentos_serializer = DepartamentoSerializer(departamentos, many=True)
        data = serializer.data
        data['Departamentos'] = departamentos_serializer.data
        return Response(data)

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        municipios = Municipio.objects.filter(IdDepartamento=instance)
        municipios_serializer = MunicipioSerializer(municipios, many=True)
        data = serializer.data
        data['Municipios'] = municipios_serializer.data
        return Response(data)

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class SectorEmpresarialViewSet(viewsets.ModelViewSet):
    queryset = SectorEmpresarial.objects.all()
    serializer_class = SectorEmpresarialSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class TipoActividadUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoActividadUsuario.objects.all()
    serializer_class = TipoActividadUsuarioSerializer

class MonedaViewSet(viewsets.ModelViewSet):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer

class CategoriasEmpleosViewSet(viewsets.ModelViewSet):
    queryset = CategoriasEmpleos.objects.all()
    serializer_class = CategoriasEmpleosSerializer

class CategoriaProyectosViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProyectos.objects.all()
    serializer_class = CategoriaProyectosSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class InstitucionEducativaViewSet(viewsets.ModelViewSet):
    queryset = InstitucionEducativa.objects.all()
    serializer_class = InstitucionEducativaSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Proyecto.objects.filter(IdUsuario=0)
        return Proyecto.objects.all()

class PostulacionEmpleoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PostulacionEmpleo.objects.all()
    serializer_class = PostulacionEmpleoSerializer

    def get_queryset(self):
        if self.action == 'list':
            return PostulacionEmpleo.objects.filter(IdEmpresa=0)
        return PostulacionEmpleo.objects.all()