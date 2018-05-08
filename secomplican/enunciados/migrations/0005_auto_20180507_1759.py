# Generated by Django 2.0.5 on 2018-05-07 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0004_auto_20180507_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionTextoSolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('solucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versiones', to='enunciados.Solucion')),
            ],
            options={
                'ordering': ['-tiempo'],
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='VersionTexto',
            new_name='VersionTextoEnunciado',
        ),
    ]