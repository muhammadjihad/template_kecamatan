# Generated by Django 2.2.2 on 2019-06-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan_publik', '0008_perizinanacara'),
    ]

    operations = [
        migrations.AddField(
            model_name='perizinanacara',
            name='approve_kecamatan',
            field=models.BooleanField(default=False),
        ),
    ]
