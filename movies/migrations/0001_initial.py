# Generated by Django 4.2 on 2023-05-01 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('sinopsis', models.TextField()),
                ('duracion', models.PositiveIntegerField()),
                ('imagen', models.ImageField(upload_to='movies/images/')),
                ('anyo', models.PositiveIntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.director')),
            ],
        ),
    ]
