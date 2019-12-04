# Generated by Django 2.2.7 on 2019-12-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='automoveis_fotos')),
                ('alugado', models.BooleanField(default=False)),
            ],
        ),
    ]
