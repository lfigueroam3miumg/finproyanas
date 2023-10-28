from django.db import models
from django.contrib.auth.models import User
from generales.models import TipoUsuario, Pais, Departamento, Municipio, InstitucionEducativa, Empresa, CategoriaProyectos, CategoriasEmpleos, Moneda
import os
import uuid
from django.utils.text import get_valid_filename

def generar_nombre_uniq(ruta_de_destino, instance, filename):
    if filename:
        _, ext = os.path.splitext(filename)
        nombre_original = get_valid_filename(os.path.basename(filename))
        nombre_uniq = f'{nombre_original}_{uuid.uuid4()}{ext}'
        return os.path.join(ruta_de_destino, nombre_uniq)
    return filename

class InfoUsuario(models.Model):
    IdInfoUsuario = models.AutoField(primary_key=True, db_column='IdInfoUsuario')
    IdUsuario = models.OneToOneField(User, on_delete=models.CASCADE, db_column='IdUsuario')
    IdTipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='IdTipoUsuario')
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='IdMunicipio')
    IdInstitucionEducativa = models.ForeignKey(InstitucionEducativa, on_delete=models.CASCADE, db_column='IdInstitucionEducativa', default=1)
    IdEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='IdEmpresa', default=1)
    CorreoInstitucional = models.CharField(max_length=250)
    Agnio = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    FechaNacimiento = models.DateField()
    Carnet = models.CharField(max_length=100, null=True, blank=True)
    FotoPerfil = models.ImageField(upload_to='fotos-perfil/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.IdInfoUsuario:
            self.FotoPerfil.name = generar_nombre_uniq('fotos-perfil/', self, self.FotoPerfil.name)
        super(InfoUsuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.CorreoInstitucional

    class Meta:
        db_table = 'InfoUsuario'

class Proyecto(models.Model):
    IdProyecto = models.AutoField(primary_key=True, db_column='IdProyecto')
    IdUsuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='IdUsuario')
    IdCategoriaProyecto = models.ForeignKey(CategoriaProyectos, on_delete=models.CASCADE, db_column='IdCategoriaProyecto')
    Estado = models.BooleanField(default=False)
    Tipo = models.IntegerField()
    Titulo = models.CharField(max_length=250)
    Descripcion = models.TextField()
    AutoresCV = models.FileField(upload_to='autores-cv/', null=True, blank=True)
    DocAceptacion = models.FileField(upload_to='documentos-aceptacion/', null=True, blank=True)
    DocClasificacion = models.FileField(upload_to='documentos-clasificacion/', null=True, blank=True)
    DocTipificacion = models.FileField(upload_to='documentos-tipificacion/', null=True, blank=True)
    DocIdentificacion = models.FileField(upload_to='documentos-identificacion/', null=True, blank=True)
    AvalEducativo = models.FileField(upload_to='avales-educativo/', null=True, blank=True)
    BriefProyecto = models.FileField(upload_to='brief-proyectos/', null=True, blank=True)
    LienzoCanva = models.FileField(upload_to='lienzos-canva/', null=True, blank=True)
    DocAPA = models.FileField(upload_to='documentos-apa/', null=True, blank=True)
    ProFinanciera = models.FileField(upload_to='documentos-financieros/', null=True, blank=True)
    Presentacion = models.FileField(upload_to='presentaciones/', null=True, blank=True)
    Video = models.FileField(upload_to='videos/', null=True, blank=True)
    FechaPublicacion = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.IdProyecto:
            self.AutoresCV.name = generar_nombre_uniq('autores-cv/', self, self.AutoresCV.name)
            self.DocAceptacion.name = generar_nombre_uniq('documentos-aceptacion/', self, self.DocAceptacion.name)
            self.DocClasificacion.name = generar_nombre_uniq('documentos-clasificacion/', self, self.DocClasificacion.name)
            self.DocTipificacion.name = generar_nombre_uniq('documentos-tipificacion/', self, self.DocTipificacion.name)
            self.DocIdentificacion.name = generar_nombre_uniq('documentos-identificacion/', self, self.DocIdentificacion.name)
            self.AvalEducativo.name = generar_nombre_uniq('avales-educativo/', self, self.AvalEducativo.name)
            self.BriefProyecto.name = generar_nombre_uniq('brief-proyectos/', self, self.BriefProyecto.name)
            self.LienzoCanva.name = generar_nombre_uniq('lienzos-canva/', self, self.LienzoCanva.name)
            self.DocAPA.name = generar_nombre_uniq('documentos-apa/', self, self.DocAPA.name)
            self.ProFinanciera.name = generar_nombre_uniq('documentos-financieros/', self, self.ProFinanciera.name)
            self.Presentacion.name = generar_nombre_uniq('presentaciones/', self, self.Presentacion.name)
            self.Video.name = generar_nombre_uniq('videos/', self, self.Video.name)
        super(Proyecto, self).save(*args, **kwargs)

    def __str__(self):
        return self.Titulo

    class Meta:
        db_table = 'Proyecto'

class PostulacionEmpleo(models.Model):
    IdPostulacionEmpleo = models.AutoField(primary_key=True, db_column='IdPostulacionEmpleo')
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='IdMunicipio')
    IdEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='IdEmpresa')
    IdCategoriasEmpleos = models.ForeignKey(CategoriasEmpleos, on_delete=models.CASCADE, db_column='IdCategoriasEmpleos')
    Estado = models.BooleanField(default=False)
    Postulacion = models.CharField(max_length=200)
    Descripcion = models.TextField()
    IdMoneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, db_column='IdMoneda')
    OfertaSalarialI = models.DecimalField(max_digits=10, decimal_places=2)
    OfertaSalarialF = models.DecimalField(max_digits=10, decimal_places=2)
    RequisitosExtra = models.FileField(upload_to='requisitos-extra/', null=True, blank=True)
    FechaPublicacion = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.IdPostulacionEmpleo:
            self.RequisitosExtra.name = generar_nombre_uniq('requisitos-extra//', self, self.RequisitosExtra.name)
        super(PostulacionEmpleo, self).save(*args, **kwargs)

    def __str__(self):
        return self.Postulacion

    class Meta:
        db_table = 'PostulacionEmpleo'