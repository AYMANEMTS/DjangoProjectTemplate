# Generated by Django 4.1.6 on 2023-02-11 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='categori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cakeapp.qatego'),
        ),
    ]
