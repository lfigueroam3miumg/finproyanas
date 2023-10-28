from django.db import models
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

class Pais(models.Model):
    IdPais = models.AutoField(primary_key=True, db_column='IdPais')
    NombreCorto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Pais'

class Departamento(models.Model):
    IdDepartamento = models.AutoField(primary_key=True, db_column='IdDepartamento')
    NombreCorto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=250)
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Departamento'

class Municipio(models.Model):
    IdMunicipio = models.AutoField(primary_key=True, db_column='IdMunicipio')
    NombreCorto = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=250)
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Municipio'

class SectorEmpresarial(models.Model):
    IdSectorEmpresarial = models.AutoField(primary_key=True, db_column='IdSectorEmpresarial')
    Nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.Nombre
    
    class Meta:
        db_table = 'SectorEmpresarial'
    
class TipoUsuario(models.Model):
    IdTipoUsuario = models.AutoField(primary_key=True, db_column='IdTipoUsuario')
    Nombre = models.CharField(max_length=150)
    Estado = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'TipoUsuario'

class TipoActividadUsuario(models.Model):
    IdTipoActividadUsuario = models.AutoField(primary_key=True, db_column='IdTipoActividadUsuario')
    Nombre = models.CharField(max_length=150)
    Estado = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'TipoActividadUsuario'

class Moneda(models.Model):
    IdMoneda = models.AutoField(primary_key=True, db_column='IdMoneda')
    Simbolo = models.CharField(max_length=10)
    Descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.Simbolo

    class Meta:
        db_table = 'Moneda'

class CategoriasEmpleos(models.Model):
    IdCategoriasEmpleos = models.AutoField(primary_key=True, db_column='IdCategoriasEmpleos')
    Nombre = models.CharField(max_length=150)
    Estado = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'CategoriasEmpleos'

class CategoriaProyectos(models.Model):
    IdCategoria = models.AutoField(primary_key=True, db_column='IdCategoria')
    Nombre = models.CharField(max_length=150)
    Estado = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'CategoriaProyectos'

class Empresa(models.Model):
    IdEmpresa = models.AutoField(primary_key=True, db_column='IdEmpresa')
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='IdMunicipio')
    IdSectorEmpresarial = models.ForeignKey(SectorEmpresarial, on_delete=models.CASCADE, db_column='IdSectorEmpresarial')
    Nombre = models.CharField(max_length=250)
    Correo = models.CharField(max_length=250)
    Descripcion = models.TextField()
    Foto = models.ImageField(upload_to='empresas/fotos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.IdEmpresa:
            self.Foto.name = generar_nombre_uniq('empresas/fotos/', self, self.Foto.name)
        super(Empresa, self).save(*args, **kwargs)

    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'Empresa'

class InstitucionEducativa(models.Model):
    IdInstitucionEducativa = models.AutoField(primary_key=True, db_column='IdInstitucionEducativa')
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='IdPais')
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='IdDepartamento')
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='IdMunicipio')
    Universidad = models.BooleanField()
    Nombre = models.CharField(max_length=250)
    Correo = models.CharField(max_length=250)
    Descripcion = models.TextField()
    Foto = models.ImageField(upload_to='instituciones/fotos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.IdInstitucionEducativa:
            self.Foto.name = generar_nombre_uniq('instituciones/fotos/', self, self.Foto.name)
        super(InstitucionEducativa, self).save(*args, **kwargs)

    def __str__(self):
        return self.Nombre
    
    class Meta:
        db_table = 'InstitucionEducativa'