# Generated by Django 4.1.6 on 2023-02-13 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0004_cake_big_descri'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComandForminTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]