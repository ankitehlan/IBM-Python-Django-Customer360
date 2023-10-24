# Generated by Django 4.2.4 on 2023-10-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='social_media',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='channel',
            field=models.CharField(choices=[('phone', 'Phone'), ('sms', 'SMS'), ('email', 'Email'), ('letter', 'Letter'), ('social_media', 'Social Media')], max_length=15),
        ),
    ]
