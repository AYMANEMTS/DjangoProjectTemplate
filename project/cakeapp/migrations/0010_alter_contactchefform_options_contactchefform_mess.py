# Generated by Django 4.1.6 on 2023-02-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0009_contactchefform'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactchefform',
            options={'verbose_name': 'Contact Chef', 'verbose_name_plural': 'Contact Form'},
        ),
        migrations.AddField(
            model_name='contactchefform',
            name='mess',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]