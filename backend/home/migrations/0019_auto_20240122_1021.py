# Generated by Django 2.2.28 on 2024-01-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_altmeasure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altmeasure',
            name='seq',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
