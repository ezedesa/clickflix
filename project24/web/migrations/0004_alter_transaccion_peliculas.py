# Generated by Django 4.2.8 on 2024-06-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_transaccion_peliculas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='peliculas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.pelicula'),
        ),
    ]
