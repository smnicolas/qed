# Generated by Django 3.0.5 on 2020-04-22 20:48

from django.db import migrations, models
from enunciados.models import conjunto_de_enunciados_file_path


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0029_renombrar_arquitecturas_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='conjuntodeenunciados',
            name='archivo',
            field=models.FileField(null=True, upload_to=conjunto_de_enunciados_file_path),
        ),
    ]