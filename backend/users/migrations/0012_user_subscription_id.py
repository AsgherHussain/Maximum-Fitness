# Generated by Django 2.2.28 on 2024-04-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
