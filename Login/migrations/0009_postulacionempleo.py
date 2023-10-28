# Generated by Django 3.2 on 2023-10-28 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0008_rename_nombres_sectorempresarial_nombre'),
        ('Login', '0008_alter_proyecto_autorescv'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostulacionEmpleo',
            fields=[
                ('IdPostulacionEmpleo', models.AutoField(db_column='IdPostulacionEmpleo', primary_key=True, serialize=False)),
                ('Postulacion', models.CharField(max_length=200)),
                ('Descripcion', models.TextField()),
                ('OfertaSalarialI', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OfertaSalarialF', models.DecimalField(decimal_places=2, max_digits=10)),
                ('RequisitosExtra', models.FileField(blank=True, null=True, upload_to='requisitos-extra/')),
                ('FechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('IdCategoriasEmpleos', models.ForeignKey(db_column='IdCategoriasEmpleos', on_delete=django.db.models.deletion.CASCADE, to='generales.categoriasempleos')),
                ('IdDepartamento', models.ForeignKey(db_column='IdDepartamento', on_delete=django.db.models.deletion.CASCADE, to='generales.departamento')),
                ('IdEmpresa', models.ForeignKey(db_column='IdEmpresa', on_delete=django.db.models.deletion.CASCADE, to='generales.empresa')),
                ('IdMoneda', models.ForeignKey(db_column='IdMoneda', on_delete=django.db.models.deletion.CASCADE, to='generales.moneda')),
                ('IdMunicipio', models.ForeignKey(db_column='IdMunicipio', on_delete=django.db.models.deletion.CASCADE, to='generales.municipio')),
                ('IdPais', models.ForeignKey(db_column='IdPais', on_delete=django.db.models.deletion.CASCADE, to='generales.pais')),
            ],
            options={
                'db_table': 'PostulacionEmpleo',
            },
        ),
    ]