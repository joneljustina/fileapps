# Generated by Django 2.1.7 on 2019-03-31 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='livroEntrada',
            fields=[
                ('numeroEntrada', models.IntegerField()),
                ('dataEntrada', models.DateField(verbose_name='Introduza a data de entrada do documento')),
                ('numeroDocumento', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='livroSaida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroOrdem', models.CharField(max_length=100)),
                ('livroEntrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.livroEntrada')),
            ],
        ),
    ]