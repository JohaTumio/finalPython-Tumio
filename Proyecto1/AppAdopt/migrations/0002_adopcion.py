# Generated by Django 4.2.5 on 2023-10-22 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdopt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppAdopt.animal')),
            ],
        ),
    ]