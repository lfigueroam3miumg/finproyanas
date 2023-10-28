
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import InfoUsuario, Proyecto, PostulacionEmpleo
from generales.models import TipoUsuario, Pais, Departamento, Municipio, InstitucionEducativa, Empresa
import traceback



# Create your views here.
def helloWorld(request):
    return render(request,'index.html')

def LoginPage(request):
    if request.method == 'GET':
        return render(request,'Pages/Login.html')
    else:
        user = authenticate(request,username=request.POST['userName'],password=request.POST['password'])
        if user is None:
            return render(request,'Pages/Login.html',{
                'error': 'Usuario o Contraseña es Incorrecto!'
            })
        else:
            login(request,user)
            return redirect('home_page')

def homePage(request):
    infoUsuario = InfoUsuario.objects.filter(IdUsuario=request.user.id).values('IdUsuario', 'IdEmpresa', 'IdTipoUsuario', 'FotoPerfil')
    tipoUsuario = TipoUsuario.objects.filter(IdTipoUsuario=infoUsuario[0]['IdTipoUsuario']).values('IdTipoUsuario', 'Nombre')
    proyectos = Proyecto.objects.filter(IdUsuario=request.user.id,Estado=True).select_related('IdCategoriaProyecto')
    empleos = PostulacionEmpleo.objects.filter(IdEmpresa=infoUsuario[0]['IdEmpresa'],Estado=True).select_related('IdPais', 'IdDepartamento', 'IdMunicipio', 'IdEmpresa', 'IdCategoriasEmpleos', 'IdMoneda')

    return render(request,'Pages/home.html',{'info': infoUsuario[0], 'tipo': tipoUsuario[0], 'proyectos': proyectos, 'empleos': empleos})

def SingUpPage(request):
    if request.method =='GET':
        tipos_usuarios = TipoUsuario.objects.filter(Estado=True).values('IdTipoUsuario', 'Nombre')
        instituciones_educativas = InstitucionEducativa.objects.all().exclude(IdInstitucionEducativa=1).values('IdInstitucionEducativa', 'Nombre')

        return render(request,'Pages/SignUp.html', {'tipos_usuarios': tipos_usuarios, 'instituciones_educativas': instituciones_educativas})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['user_name'],email=request.POST['correo'],password=request.POST['password1'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
                user.save()
                
                tipo_usuario = TipoUsuario.objects.get(IdTipoUsuario=int(request.POST['tipo_usuario']))
                pais = Pais.objects.get(IdPais=int(request.POST['pais']))
                departamento = Departamento.objects.get(IdDepartamento=int(request.POST['departamento']))
                municipio = Municipio.objects.get(IdMunicipio=int(request.POST['municipio']))
                institucion_educativa = InstitucionEducativa.objects.get(IdInstitucionEducativa=int(request.POST['institucion_educativa']))
                empresa = Empresa.objects.get(IdEmpresa=1)

                info_usuario = InfoUsuario(
                    IdUsuario=user,
                    IdTipoUsuario=tipo_usuario,
                    IdPais=pais,
                    IdDepartamento=departamento,
                    IdMunicipio=municipio,
                    IdInstitucionEducativa=institucion_educativa,
                    IdEmpresa=empresa,
                    CorreoInstitucional=request.POST['correo'],
                    Agnio=request.POST['agnio'],
                    Telefono=request.POST['celular'],
                    FechaNacimiento=request.POST['fecha'],
                    Carnet=request.POST['carnet'],
                    FotoPerfil=request.FILES['foto_perfil']
                )

                info_usuario.save()
                print(info_usuario)
                return redirect('login_page')
            except Exception as e:
                print(e)
                traceback.print_exc()
                return render(request, 'Pages/SignUp.html', {
                    "error": "Usuario ya Registrado!"
                })
        return render(request,'Pages/SignUp.html',{
            "error": "Las Contraseñas no Coinciden!"
        })

def projectPage(request):
    infoUsuario = InfoUsuario.objects.filter(IdUsuario=request.user.id).values('IdUsuario', 'IdTipoUsuario', 'FotoPerfil')
    tipoUsuario = TipoUsuario.objects.filter(IdTipoUsuario=infoUsuario[0]['IdTipoUsuario']).values('IdTipoUsuario', 'Nombre')
    proyectos = Proyecto.objects.filter(Estado=True).select_related('IdCategoriaProyecto', 'IdUsuario')

    return render(request,'Pages/Proyectos.html',{'info': infoUsuario[0], 'tipo': tipoUsuario[0], 'proyectos': proyectos})

def jobsPage(request):
    infoUsuario = InfoUsuario.objects.filter(IdUsuario=request.user.id).values('IdUsuario', 'IdTipoUsuario', 'FotoPerfil')
    tipoUsuario = TipoUsuario.objects.filter(IdTipoUsuario=infoUsuario[0]['IdTipoUsuario']).values('IdTipoUsuario', 'Nombre')
    empleos = PostulacionEmpleo.objects.filter(Estado=True).select_related('IdPais', 'IdDepartamento', 'IdMunicipio', 'IdEmpresa', 'IdCategoriasEmpleos', 'IdMoneda')

    return render(request,'Pages/BolsaTrabajo.html',{'info': infoUsuario[0], 'tipo': tipoUsuario[0], 'empleos': empleos})

def helpPage(request):
    infoUsuario = InfoUsuario.objects.filter(IdUsuario=request.user.id).values('IdUsuario', 'IdTipoUsuario', 'FotoPerfil')
    tipoUsuario = TipoUsuario.objects.filter(IdTipoUsuario=infoUsuario[0]['IdTipoUsuario']).values('IdTipoUsuario', 'Nombre')

    return render(request,'Pages/espacioApoyo.html',{'info': infoUsuario[0], 'tipo': tipoUsuario[0]})

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')