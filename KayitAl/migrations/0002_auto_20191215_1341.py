# Generated by Django 2.2.5 on 2019-12-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KayitAl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kayitmodels',
            name='cinsiyet',
            field=models.CharField(choices=[('0', 'ERKEK'), ('1', 'KADIN')], max_length=15),
        ),
    ]