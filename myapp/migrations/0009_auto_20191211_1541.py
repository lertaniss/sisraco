# Generated by Django 2.2.4 on 2019-12-11 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20191203_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordenadas',
            name='cor_oni_codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bus', to='myapp.Onibus'),
        ),
    ]
