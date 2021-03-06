# Generated by Django 2.2.7 on 2019-12-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='clientes_fotos')),
            ],
        ),
    ]
