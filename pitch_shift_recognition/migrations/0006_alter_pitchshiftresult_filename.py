# Generated by Django 4.2.5 on 2023-10-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitch_shift_recognition', '0005_alter_pitchshiftresult_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchshiftresult',
            name='filename',
            field=models.FilePathField(null=True, path='pitch_shift_recognition/output_files/'),
        ),
    ]
