# Generated by Django 4.1.6 on 2023-02-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('descri', models.TextField(blank=True, max_length=1000, null=True)),
                ('cake_img', models.ImageField(blank=True, null=True, upload_to='imgs_cake/')),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('spes', models.TextField(blank=True, max_length=300, null=True)),
                ('chef_img', models.ImageField(blank=True, null=True, upload_to='imgs_chef/')),
            ],
        ),
        migrations.CreateModel(
            name='Qatego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
