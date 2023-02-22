# Generated by Django 4.0.4 on 2023-02-22 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MarcaMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoFarmaco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ViaAdminstracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('medida', models.CharField(max_length=10)),
                ('fecha_vencimento', models.DateField()),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.laboratorio')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.marcamedicamento')),
                ('tipoFarmaco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipofarmaco')),
                ('viaAdmin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.viaadminstracion')),
            ],
        ),
    ]
