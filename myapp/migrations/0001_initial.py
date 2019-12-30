# Generated by Django 2.2.3 on 2019-08-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=20, max_digits=20)),
                ('y', models.DecimalField(decimal_places=20, max_digits=20)),
            ],
            options={
                'db_table': 'coordenadas',
            },
        ),
    ]
