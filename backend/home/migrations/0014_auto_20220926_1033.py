# Generated by Django 2.2.28 on 2022-09-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20220926_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvideo',
            name='video_thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='post_video/thumbnail'),
        ),
    ]