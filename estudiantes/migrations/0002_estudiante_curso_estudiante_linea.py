# Generated by Django 5.1.5 on 2025-02-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='curso',
            field=models.IntegerField(null=True, verbose_name='curso'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='linea',
            field=models.CharField(max_length=255, null=True, verbose_name='linea'),
        ),
    ]
