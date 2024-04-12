# Generated by Django 5.0.4 on 2024-04-12 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('mymodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signals.mymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Order3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('mymodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signals.mymodel')),
            ],
        ),
    ]