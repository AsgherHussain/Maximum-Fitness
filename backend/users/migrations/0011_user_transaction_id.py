# Generated by Django 2.2.28 on 2024-04-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_is_premium_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
