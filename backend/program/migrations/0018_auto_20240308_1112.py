# Generated by Django 2.2.28 on 2024-03-08 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0017_auto_20240307_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customworkout',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]