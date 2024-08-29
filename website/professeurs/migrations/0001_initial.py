# Generated by Django 5.1 on 2024-08-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professeurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('date_de_creation', models.DateField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('vacant', models.BooleanField(max_length=50)),
                ('matiere_enseigne', models.CharField(max_length=50)),
                ('prochain_cours', models.CharField(max_length=50)),
                ('sujet_prochaincours', models.CharField(max_length=50)),
            ],
        ),
    ]
