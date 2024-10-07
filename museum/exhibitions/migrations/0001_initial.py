# Generated by Django 5.0.6 on 2024-10-07 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artworks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitionArtWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artworks.artwork')),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibitions.exhibition')),
            ],
        ),
    ]
